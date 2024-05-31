import random

from value import Value

class Neuron:
    def __init__(self, num_in):
        self.w = [Value(random.uniform(-1,1)) for _ in range(num_in)]
        self.b = Value(random.uniform(-1,1))
        
    def __call__(self, x):
        act = sum(((wi*xi) for wi, xi in zip(self.w, x)), self.b)
        out = act.tanh()
        
        return out

class Layer:
    def __init__(self, num_in, num_out):
        self.neurons = [Neuron(num_in) for _ in range(num_out)]
    
    def __call__(self, x):
        outs = [n(x) for n in self.neurons]
        
        return outs

class MLP:
    def __init__(self, num_in, num_outs):
        size = [num_in] + num_outs
        self.layers = [Layer(size[i], size[i+1]) for i in range(len(num_outs))]
    
    def __call__(self, x):
        for layer in self.layers:
            x = layer(x)
        
        return x