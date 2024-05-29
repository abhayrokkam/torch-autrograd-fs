import math

class Value:
    def __init__(self, data, label = '', _op = '', _prev = (), grad = 0):
        self.data = data
        self.label = label
        self._op = _op
        self._prev = set(_prev)
        self.grad = grad
        self._backward = lambda : None
    
    # Representation of class while print()
    def __repr__(self):
        return f'Value(data:{self.data}, label:{self.label})'
    
    def __add__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        sum = self.data + other.data
        val = Value(sum, _op = '+', _prev=(self, other))
        
        def _backward():
            self.grad += val.grad
            other.grad += val.grad
        val._backward = _backward
        
        return val
    
    def __radd__(self, other): # recieving -> (other + self) in terms of __add__
        return self + other
    
    def __mul__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        prod = self.data * other.data
        val = Value(prod, _op = '*', _prev=(self, other))
        
        def _backward():
            self.grad += other.data * val.grad
            other.grad += self.data * val.grad
        val._backward = _backward
        
        return val
    
    def __rmul__(self, other): # recieving -> (other * self) in terms of __mul__
        return self * other
    
    def __neg__(self):
        return self * -1
    
    def __sub__(self, other):
        return self + (-other)
    
    def __pow__(self, other):
        assert isinstance(other, (int, float)) # only int, float values are supported
        res = self.data ** other
        val = Value(res, _op = f'**{other}', _prev = (self, ))
        
        def _backward():
            self.grad += other * (self.data ** (other - 1)) * val.grad
        val._backward = _backward
        
        return val
    
    def __truediv__(self, other):
        return self * (other ** -1)
    
    def exp(self):
        res = math.exp(self.data)
        val = Value(res, _op = 'exp', _prev = (self, ))
        
        def _backward():
            self.grad += res * val.grad
        val._backward = _backward
        
        return val
    
    def tanh(self):
        res = (math.exp(2 * self.data) - 1) / (math.exp(2 * self.data) + 1)
        val = Value(res, _op = 'tanh', _prev = (self, ))
        
        def _backward():
            self.grad += (1 - res**2) * val.grad
        val._backward = _backward
        
        return val    
    
    # Function which back propogates from the given point and sets the gradients
    def back_prop(self):
        topo = []
        visited = set()
        
        def build_topo(v):
            if v not in visited:
                visited.add(v)
                for child in v._prev:
                    build_topo(child)
                topo.append(v)
        
        build_topo(self)
        self.grad = 1.0
        for node in reversed(topo):
            node._backward()