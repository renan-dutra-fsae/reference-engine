import numpy as np

# The Frame class represents a reference frame in 2D space, defined by its origin and rotation. 
# It can have a parent frame and multiple child frames, allowing for hierarchical relationships between frames. 
# The class provides a method to translate the frame by a given translation vector.

class Frame:

    def __init__(self, name, origin=None, rotation=None, parent=None):

        self.name = name

        self.origin = np.zeros(2) if origin is None else origin
        self.rotation = np.eye(2) if rotation is None else rotation

        self.parent = parent
        self.children = []

        if parent is not None:
            parent.children.append(self)

    def translate(self, translation):
        self.origin += translation