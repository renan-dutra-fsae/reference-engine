import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from reference_engine import Frame, Body, World

GRAVITY = np.array([0.0, -9.81])

world = World(gravity=GRAVITY, world_origin=np.array([0.0, 0.0]))

position = np.array([0.0, 100.0])

ball = world.add_body("ball", mass=1.0, parent_frame=world.world_frame, origin=position)

fig, ax = plt.subplots()

ball_fig = Circle((ball.frame.origin[0], ball.frame.origin[1]), radius=5)

ax.add_patch(ball_fig)

ax.set_xlim(-50, 50)
ax.set_ylim(-120, 120)
ax.set_aspect("equal")

plt.show()