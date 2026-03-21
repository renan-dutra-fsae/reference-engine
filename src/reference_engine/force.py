from abc import abstractmethod
from reference_engine.geometry import Vector
from reference_engine.body import Body

class Force:

    def __init__(self, name, force_vector):
        self.name = name
        assert isinstance(force_vector, Vector), f"Vector must be a Vector, got {type(force_vector)}"
        self.vector = force_vector
        self.direction = force_vector.normalize()
        self.bodies = []
    
    def __add__(self, other):
        if not isinstance(other, Force):
            raise ValueError(f"Can only add Force to Force, got {type(other)}")
        new_vector = self.vector + other.vector
        return Force(f"{self.name} + {other.name}", new_vector)
    
    def __mul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise ValueError(f"Can only multiply Force by scalar, got {type(scalar)}")
        new_vector = self.vector * scalar
        return Force(f"{self.name} * {scalar}", new_vector)
    
    def __truediv__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise ValueError(f"Can only divide Force by scalar, got {type(scalar)}")
        if scalar == 0:
            raise ValueError("Cannot divide Force by zero")
        new_vector = self.vector / scalar
        return Force(f"{self.name} / {scalar}", new_vector)
    
    def __sub__(self, other):
        if not isinstance(other, Force):
            raise ValueError(f"Can only subtract Force from Force, got {type(other)}")
        new_vector = self.vector - other.vector
        return Force(f"{self.name} - {other.name}", new_vector)

    def apply(self):
        for body in self.bodies:
            body.apply_force(self.vector)

    @abstractmethod
    def set(self): pass

class Gravity(Force):
    
    def __init__(self, name, force_vector = Vector(0.0, 0.0, -9.81)):
        super().__init__(name, force_vector)
    
    def set(self, body):
        if not isinstance(body, Body) :
            raise ValueError("Body must be of type Body")
        self.bodies.append(body)


