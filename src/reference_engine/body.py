import numpy as np
from abc import ABC, abstractmethod 
from reference_engine.geometry import Point, Vector
from reference_engine import Frame 


#Body class represents a physical object with mass, velocity, and acceleration. 
# It is an abstract base class that defines the interface for specific types of bodies, such as rigid bodies and particles.
# The RigidBody class is a specific type of Body that represents a rigid object. 
# It has a position defined by a reference frame and a velocity vector.
# The Particle class is another type of Body that represents a point mass. 
# It has a position defined by a Point and a velocity defined by a Vector.


class Body:

    def __init__(self, name, mass=0.0):
        self.name = name
        self.mass = mass
        self.resultant = Vector(0.0, 0.0, 0.0)

    def apply_force(self, force):
        self.resultant += force

    def clear_forces(self):
        self.resultant = Vector(0.0, 0.0, 0.0)

    def get_net_force(self):
        return self.resultant

    @abstractmethod
    def set_velocity(self, velocity): pass

    @abstractmethod
    def get_velocity(self): pass
        
    @abstractmethod
    def set_position(self, position): pass

    @abstractmethod
    def get_position(self): pass

class RigidBody(Body):

    def __init__(self, name, mass=0.0, parent_frame=None, origin=None, angular_velocity=None):
        super().__init__(name, mass)
        assert isinstance(origin, Frame), f"Origin must be a Frame, got {type(origin)}"
        assert isinstance(parent_frame, Frame), f"Parent frame must be a Frame, got {type(parent_frame)}"
        self.position = Frame(name + "_frame", origin, parent=parent_frame)
        self.velocity = None
        self.omega = angular_velocity

        def set_velocity(self, velocity):
            if not isinstance(velocity, Vector):
                raise ValueError(f"Velocity must be a Vector, got {type(velocity)}")
            self.velocity = velocity

        def get_velocity(self):
            return self.velocity

        def set_position(self, position):
            if not isinstance(position, Point):
                raise ValueError(f"Position must be a Point, got {type(position)}")
            self.frame.origin = position

        def get_position(self):
            return self.frame.origin

class Particle(Body):

    def __init__(self, name, mass=0.0, position_point=None, velocity= Vector(0,0,0)):
        super().__init__(name, mass)
        assert isinstance(position_point, Point), f"Position must be a Point, got {type(position_point)}"
#       assert isinstance(velocity_vector, Vector), f"Velocity must be a Vector, got {type(velocity_vector)}"   NOT NEEDED
        self.position = position_point.copy()
        self.x = position_point.x
        self.y = position_point.y
        self.z = position_point.z
        self.prev_position = self.position.copy()
        self.velocity = velocity.copy()

    def set_velocity(self, dt):
        self.velocity = (self.position - self.prev_position) / dt
    
    def get_velocity(self,dt):
        self.set_velocity(dt)
        return self.velocity
    
    def set_position(self, position):
        if not isinstance(position, Point):
            raise ValueError(f"Position must be a Point, got {type(position)}")
        self.position = position
    
    def get_position(self):
        return self.position

    