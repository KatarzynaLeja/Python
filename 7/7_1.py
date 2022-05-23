class Vector:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self): # return string "Vector(x, y, z)"
        return f'Vector({self.x}, {self.y}, {self.z})'

    def __eq__(self, other):
        if type(other) == int:
            return other
        else:
            return self.x - other.x == 0 and self.y - other.y == 0 and self.z - other.z == 0

    def __ne__(self, other):        # v != w
        return not self == other

    def __add__(self, other):   # v + w
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):   # v - w
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):  # return the dot product (number)
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def cross(self, other):    # return the cross product (Vector)
        return Vector(self.y*other.z - self.z * other.y,
        self.z * other.x - self.x * other.z,
        self.x * other.y - self.y * other.x)
    
    def length(self):  # the length of the vector
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    def __hash__(self):   # we assume that vectors are immutable
        return hash((self.x, self.y, self.z))   # recommended

import math

v = Vector(1, 1, 3)
w = Vector(1, 1, 1)

def find_axis(v1, v2):
    X = v1.cross(v2)
    l = X.length()
    if l == 0:
        raise ValueError('Vectors are parallel')
    elif v1.length == 0 or v2.length == 0:
        raise ValueError('v1 or v2 is equal to 0')
    else:
        return Vector(X.x/l, X.y/l, X.z/l)


print(find_axis(v, w))
