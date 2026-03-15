import numpy as np

class Frame:

    def __init__(self, name, origin=None, rotation=None, parent=None):

        self.name = name

        self.origin = np.zeros(3) if origin is None else origin
        self.rotation = np.eye(3) if rotation is None else rotation

        self.parent = parent
        self.children = []

        if parent is not None:
            parent.children.append(self)