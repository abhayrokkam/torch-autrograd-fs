import math

class Value:
    def __init__(self, data, label = '', _op = '', _prev = (), grad = 0):
        self.data = data
        self.label = label
        self._op = _op
        self._prev = list(_prev)
        self.grad = grad
        self._backward = lambda : None
    
    # Representation of class while print()
    def __repr__(self):
        return f'Value(data:{self.data}, label:{self.label})'
    
    def __add__(self, other):
        sum = self.data + other.data
        val = Value(sum, _op = '+', _prev=(self, other))
        
        def _backward():
            self.grad = val.grad
            other.grad = val.grad
        val._backward = _backward
        
        return val
    
    def __mul__(self, other):
        prod = self.data * other.data
        val = Value(prod, _op = '*', _prev=(self, other))
        
        def _backward():
            self.grad = other.data * val.grad
            other.grad = self.data * val.grad
        val._backward = _backward
        
        return val
    
    def tanh(self):
        res = (math.exp(2 * self.data) - 1) / (math.exp(2 * self.data) + 1)
        val = Value(res, _op = 'tanh', _prev = (self, ))
        
        def _backward():
            self.grad = (1 - res**2) * val.grad
        val._backward = _backward
        
        return val
    
    def back_prop(self):
        final_to_initial = []
        
        def store_children(x):
            final_to_initial.append(x)
            for child in x._prev:
                store_children(child)
        
        store_children(self)
        self.grad = 1
        for ele in final_to_initial:
            ele._backward()