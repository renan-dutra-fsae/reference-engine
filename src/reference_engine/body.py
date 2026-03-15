import numpy as np

class Body:

    def __init__(self, name, mass=0.0, frame=None):

        self.name = name
        self.mass = mass
        self.velocity = None
        self.acceleration = None
        self.position = frame

    def set_velocity(self, velocity):
        self.velocity = np.array(velocity)

    def set_acceleration(self, acceleration):
        self.acceleration = np.array(acceleration)