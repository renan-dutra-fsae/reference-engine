import numpy as np
from reference_engine import Frame
from reference_engine import Body
from reference_engine import Integrator

# The World class represents a physical simulation environment that contains multiple bodies and a global reference frame.

class World:

    def __init__(self, gravity, world_origin=None):
        self.bodies = []
        self.time = 0.0
        self.gravity = gravity
        self.integrator = Integrator()
        self.world_frame = Frame("World", world_origin if world_origin is not None else np.zeros(2))

    def add_body(self, body_name, mass=0.0, parent_frame=None, origin=None):
        body = Body(body_name, mass, parent_frame, origin)
        self.bodies.append(body)
        return body

    def step(self, dt):
        for body in self.bodies:
            if body.acceleration is None:
                body.set_acceleration(self.gravity)

            if body.velocity is None:
                body.set_velocity([0.0, 0.0])

            self.integrator.step(body, dt)

        self.time += dt