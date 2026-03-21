from reference_engine import Frame
from reference_engine import body
from reference_engine.body import Particle, RigidBody

class Integrator:

# The Integrator class provides a method to update the state of a body over a time step using simple Euler integration. 
# Should change it to runge kutta 3rd order or 4th order for better accuracy, or maybe add multiple integration methods 
# that can be selected by the user.

    def step(self, body, dt=0.01):
        if isinstance(body, Particle):
            body.velocity += body.get_net_force() / (body.mass * dt)
            body.position += body.velocity.to_point() * dt
        elif isinstance(body, RigidBody):
            pass
        else:
            raise ValueError(f"Body must be of type Particle or RigidBody, got {type(body)}")