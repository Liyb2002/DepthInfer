import numpy as np
import random

class dummy_object:
    def __init__(self, position, scope):
        self.position = position
        self.scope = scope

    def get_aabb(self):
        return {
            "min_x": self.position[0] - self.scope[0] / 2,
            "max_x": self.position[0] + self.scope[0] / 2,
            "min_y": self.position[1] - self.scope[1] / 2,
            "max_y": self.position[1] + self.scope[1] / 2,
            "min_z": self.position[2] - self.scope[2] / 2,
            "max_z": self.position[2] + self.scope[2] / 2
        }
