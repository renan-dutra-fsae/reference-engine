from reference_engine import Frame
from reference_engine import body
from reference_engine.body import Particle, RigidBody
from reference_engine.constraints import PositionConstraint

class Integrator:

# The Integrator class provides a method to update the state of a body over a time step using simple Euler integration. 
# Should change it to runge kutta 3rd order or 4th order for better accuracy, or maybe add multiple integration methods 
# that can be selected by the user.
    
    def step(self, body, dt=0.01):
        if body.mass == float('inf'):
            return

        a = body.resultant / body.mass
        acceleration = a.to_point()

        new_position = (body.position + (body.position - body.prev_position) + acceleration * (dt ** 2))

        body.prev_position = body.position
        body.position = new_position.copy()
        body.set_velocity(dt)
