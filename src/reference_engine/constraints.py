from reference_engine.geometry import Point, Vector
from reference_engine.body import Particle
from abc import abstractmethod

#  Constraints are used to enforce specific conditions on the positions and velocities of bodies in the simulation. They can be used to model joints, contacts, or any other relationships between bodies that must be maintained throughout the simulation.
# The Constraints class is a base class that defines the interface for specific types of constraints, such as PositionConstraint and VelocityConstraint.
# The PositionConstraint class is used to enforce a specific position relationship between two bodies, while the VelocityConstraint class is used to 
# enforce a specific velocity relationship between two bodies. Both classes take two bodies as input, along with the specific points or velocities that 
# define the constraint. They try to undo what the forces do to the bodies to maintain the constraint, so they should be applied after all forces 
# have been applied and before the integrator step in the World.step() method.

class Constraints:
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def solve(self): pass


class PositionConstraint(Constraints):
    def __init__(self, name, p1=None, p2=None, rest_length=0.0):
        super().__init__(name)
        assert isinstance(p1, Particle), f"p1 must be a Particle, got {type(p1)}"
        assert isinstance(p2, Particle), f"p2 must be a Particle, got {type(p2)}"
        self.p1 = p1
        self.p2 = p2
        self.rest_length = rest_length


    def solve(self):
        delta = self.p2.position - self.p1.position # Direction of the error
        distance = delta.magnitude() # Distance between real position and wrong position
        if distance == 0:
            return # Avoid division by zero
        w1 = 0 if self.p1.mass == float('inf') else 1 / self.p1.mass
        w2 = 0 if self.p2.mass == float('inf') else 1 / self.p2.mass

        difference = (distance - self.rest_length) / distance # How much we need to correct the positions
        correction = (delta * difference) / ((w1 + w2)) # Correction vector scaled by mass
        self.p1.position += correction * w1 # Move p1 towards p2
        self.p2.position -= correction * w2 # Move p2 away from p1

