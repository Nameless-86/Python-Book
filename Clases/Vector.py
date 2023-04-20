class Vector:

    def __init__(self, dimension):

        self.coordenadas = [0]*dimension

    def __len__(self):
        return len(self.coordenadas)

    def __getitem__(self, j):
        return self.coordenadas[j]

    def __setitem__(self, j, val):
        self.coordenadas[j] = val

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError('Error de dimensiones')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __radd__(self, other):
        return self.__add__(other)

    def __eq__(self, other):
        return self.coordenadas == other.coordenadas

    def __ne__(self, other):
        return not self == other

    def __neg__(self):
        neg = []
        for i in range(len(self)):
            x = self.coordenadas[i]
            neg.append(-x)
        return neg

    def __mul__(self, other):
        """Defines scalar multiplication and dot product"""
        if isinstance(other, (int, float)): #Scalar multiplication
            result = Vector(len(self))
            for i in range(len(self)):
                result[i] = self[i]*other
        elif isinstance(other, Vector): #Dot product
            if len(self) != len(other):
                raise ValueError("Vectors must have same dimentions")
            result = 0
            for i in range(len(self)):
                result += self[i] * other[i]
        else:
            raise TypeError("Unsupported operand type")

        return result

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def __str__(self):
        return '<' + str(self.coordenadas)[1:-1] + '>'


v = Vector(5)
v[1] = 23
v[-1] = 45
print(v[4])
u = 3*v
w = v*u
print(w)
total = 0
for entry in v:
    total += entry

# print(Vector.__neg__(u))
