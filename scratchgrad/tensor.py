import numpy as np

class Tensor:
    def __init__(self, data):
        self.data = data
        self.shape = self.get_shape(self.data)

    def get_shape(self, data):
        print(data)


