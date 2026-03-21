import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from reference_engine.body import Particle
from reference_engine.force import Gravity
from reference_engine.world import World
from reference_engine.geometry import Point, Vector
from reference_engine.constraints import PositionConstraint 

# This example simulates a pendulum, which consists of a mass (the ball) attached to a fixed point (the anchor) by a rigid rod. 
# The ball is subject to gravity, and the position constraint ensures that the distance between the ball and the anchor remains constant, 
# simulating the effect of the rod.

x = 10.0
y = 25.0
position = Point(x, 0.0, y)
velocity = Vector(0.0, 0.0, 0.0)
g_vector = Vector(0.0, 0.0, -9.81)
world = World(world_origin=np.array([0.0, 0.0, 0.0]))
ball = world.add_particle(body_name="ball", mass=10.0, position=position, velocity=velocity)
gravity = Gravity("gravity", g_vector)
gravity.set(ball)
world.add_force(gravity)
world.set_solver_iterations(30)


anchor = world.add_particle(body_name="anchor", mass=float('inf'), position=Point(0.0, 0.0, 100.0) , velocity=Vector(0.0, 0.0, 0.0))
coord = (ball.position - anchor.position).magnitude()
constraint = world.add_position_constraint(constraint_name="Pendulum", p1=anchor, p2=ball, rest_length=coord)


fig, ax = plt.subplots()
point, = ax.plot([], [], 'ro', markersize=10)
ax.set_xlim(-10,10)
ax.set_ylim(-110,110)

dt = 0.01

# The update function is called for each frame of the animation. It advances the simulation by one time step, updates the position of the ball, and prints the current position, velocity, and net force to the console.

initial_velocity = Point(-2.0, 0.0, 0.0)

ball.prev_position = ball.position - initial_velocity * dt

def update(step):

    world.step(dt=dt)

    pos = ball.get_position()
    vel = ball.get_velocity(dt)
    f = ball.get_net_force()


    point.set_data([pos.x], [pos.z])

    print("xpos:", pos.x, "ypos:", pos.z, "xvel:", vel.x, "yvel:", vel.z, "force:", f.z)

    return point
    

ani = FuncAnimation(fig, update, frames=100, interval=20)

plt.show()