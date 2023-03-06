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

    def __str__(self):
        return '<' + str(self.coordenadas)[1:-1] + '>'


v = Vector(5)
v[1] = 23
v[-1] = 45
print(v[4])
u = v+v
print(u)
total = 0
for entry in v:
    total += entry

print(Vector.__neg__(u))
