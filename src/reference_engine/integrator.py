from reference_engine import Frame
from reference_engine import Body

class Integrator:

# The Integrator class provides a method to update the state of a body over a time step using simple Euler integration. 
# Should change it to runge kutta 3rd order or 4th order for better accuracy

    def step(self, body, dt=0.01):

        body.velocity += body.acceleration * dt
        body.frame.translate(body.velocity * dt)