import numpy as np


class Tensor:
    def __init__(self, data):
        self.data = data
        self.shape = self.get_shape(self.data)

    def get_shape(self, data):
        print(data)

    def randn(*dims):
        return np.random.standard_normal(dims)

    def ones(*dims):
        return np.ones(dims)
    
    def zeros(*dims):
        return np.zeros(dims)
    
    
    


