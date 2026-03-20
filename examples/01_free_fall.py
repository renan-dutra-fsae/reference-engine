import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import reference_engine as re

GRAVITY = np.array([0.0, -9.81])

world = re.World(gravity=GRAVITY, world_origin=np.array([0.0, 0.0]))

position = np.array([0.0, 100.0])

ball = world.add_body("ball", mass=1.0, parent_frame=world.world_frame, origin=position)

dt = 0.2

fig, ax = plt.subplots()

point, = ax.plot([], [], 'ro', markersize=10)

ax.set_xlim(-10,10)
ax.set_ylim(-110,110)


def update(step):

    world.step(dt)

    x = ball.frame.origin[0]
    y = ball.frame.origin[1]

    point.set_data([x], [y])

    return point,


ani = FuncAnimation(fig, update, frames=500, interval=20)

plt.show()