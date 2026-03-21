import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from reference_engine.force import Gravity
from reference_engine.world import World
from reference_engine.geometry import Point, Vector

# This example simulates a free fall of a particle under the influence of gravity.

position = Point(0.0, 0.0, 100.0)
velocity = Vector(0.0, 0.0, 0.0)
g_vector = Vector(0.0, 0.0, -9.81)
world = World(world_origin=np.array([0.0, 0.0]))
ball = world.add_particle(body_name="ball", mass=1.0, position=position, velocity=velocity)
gravity = Gravity("gravity", g_vector)
gravity.set(ball)
world.add_force(gravity)


fig, ax = plt.subplots()
point, = ax.plot([], [], 'ro', markersize=10)
ax.set_xlim(-10,10)
ax.set_ylim(-110,110)

dt = 0.5

# The update function is called for each frame of the animation. It advances the simulation by one time step, updates the position of the ball, and prints the current position, velocity, and net force to the console.

def update(step):

    world.step(dt)

    pos = ball.get_position()
    vel = ball.get_velocity()
    f = ball.get_net_force()
    x = pos.x
    y = pos.z

    point.set_data([x], [y])

    print("pos:", pos.z, "vel:", vel.z, "force:", f.z)

    return point
    

ani = FuncAnimation(fig, update, frames=100, interval=20)

plt.show()