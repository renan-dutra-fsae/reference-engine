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


position = Point(10, 0.0, 40)
velocity = Vector(-1.0, 0.0, 0.0)
g_vector = Vector(0.0, 0.0, -9.81)
world = World(world_origin=np.array([0.0, 0.0, 0.0]))
ball = world.add_particle(body_name="ball", mass=10.0, position=position, velocity=velocity)
gravity = Gravity("gravity", g_vector)
gravity.set(ball)
world.add_force(gravity)
world.set_solver_iterations(20)


anchor = world.add_particle(body_name="anchor", mass=float('inf'), position=Point(0.0, 0.0, 50) , velocity=Vector(0.0, 0.0, 0.0))
coord = np.sqrt(100 + 100)
constraint = world.add_position_constraint("Pendulum", anchor, ball, coord)


fig, ax = plt.subplots()
point, = ax.plot([], [], 'ro', markersize=5)
ax.set_xlim(-50,50)
ax.set_ylim(-50,50)

dt = 0.1

# The update function is called for each frame of the animation. It advances the simulation by one time step, updates the position of the ball, and prints the current position, velocity, and net force to the console.

initial_velocity = Point(-1.0, 0.0, 0.0)

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