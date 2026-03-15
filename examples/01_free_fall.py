import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from reference_engine import Frame, Body


WORLD = Frame("world", origin=np.array([0.0, 0.0]))

GRAVITY = np.array([0.0, -9.81])

position = np.array([0.0, 100.0])

ball = Body("ball", mass=1.0, parent_frame=WORLD, origin=position)

fig, ax = plt.subplots()

ball_fig = Circle((position[0], position[1]), radius=5)

ax.add_patch(ball_fig)

ax.set_xlim(-50, 50)
ax.set_ylim(-120, 120)
ax.set_aspect("equal")

plt.show()