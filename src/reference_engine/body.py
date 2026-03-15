import numpy as np
from reference_engine.frame import Frame

#Body class represents a physical object with mass, velocity, and acceleration. 
#It is associated with a reference frame that defines its position and orientation in space. 
# The class provides methods to set the velocity and acceleration of the body.

class Body:

    def __init__(self, name, mass=0.0, parent_frame=None, origin=None):
        self.name = name
        self.mass = mass
        self.velocity = None
        self.acceleration = None
        self.frame = Frame(name + "_frame", parent=parent_frame, origin=origin)

    def set_velocity(self, velocity):
        self.velocity = np.array(velocity)

    def set_acceleration(self, acceleration):
        self.acceleration = np.array(acceleration)