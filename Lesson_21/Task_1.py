import numpy as np


class Matrix:
    def __init__(self, *args):
        self.matrix = np.array(args)

    def __str__(self):
        return str(self.matrix)

    def add(self, B):
        C = self.matrix + B.matrix
        return C

    def minus(self, B):
        C = self.matrix - B.matrix
        return C

    def number_multiple(self, number):
        return self.matrix * number

    def multiple(self, B):
        C = self.matrix.dot(B.matrix)
        return C

    def transponse(self):
        return self.matrix.T


r1 = [1, 2, 3]
r2 = [3, 4, 5]
r3 = [5, 6, 7]

r4 = [2, 7, 9]
r5 = [9, 7, 5]
r6 = [4, 7, 1]

m1 = Matrix(r1, r2, r3)
m2 = Matrix(r4, r5, r6)

print(m1.add(m2))
print(m2.minus(m1))
print(m1.number_multiple(2))
print(m1.multiple(m2))
print(m2.transponse())
