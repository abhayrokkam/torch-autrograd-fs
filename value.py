class Value:
    def __init__(self, data, label = '', _op = '', _prev = (), grad = 0):
        self.data = data
        self.label = label
        self._op = _op
        self._prev = _prev
        self.grad = grad
    
    def __repr__(self):
        return f'Value(data:{self.data}, label:{self.label})'
    
    def __add__(self, other):
        sum = self.data + other.data
        return Value(sum, _op = '+', _prev=(self, other))
    
    def __mul__(self, other):
        prod = self.data * other.data
        return Value(prod, _op = '*', _prev=(self, other))