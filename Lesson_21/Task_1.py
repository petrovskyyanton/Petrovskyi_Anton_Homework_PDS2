import numpy as np


class MatrixError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        return f'Something wrong: {self.message}'

class Matrix:
    def __init__(self, lists):
        self.lists = lists
        self.matrix = np.array(lists)

    def __str__(self):
        return str(self.matrix)

    def add(self, B):
        if len(self.matrix) < len(B.matrix):
            dif = len(B.matrix) - len(self.matrix)
            q = []
            for i in range(len(self.matrix[0])):
                q.append(0)
            for i in range(dif):
                self.lists.append(q)
            self.matrix = np.array(self.lists)
        if len(self.matrix) > len(B.matrix):
            dif = len(self.matrix) - len(B.matrix)
            q = []
            for i in range(len(B.matrix[0])):
                q.append(0)
            for i in range(dif):
                B.lists.append(q)
            B.matrix = np.array(B.lists)
        if len(self.matrix[0]) < len(B.matrix[0]):
            dif = len(B.matrix[0]) - len(self.matrix[0])
            for w in range(dif):
                for i in self.lists:
                    i.append(0)
            self.matrix = np.array(self.lists)
        if len(self.matrix[0]) > len(B.matrix[0]):
            dif = len(self.matrix[0]) - len(B.matrix[0])
            for w in range(dif):
                for i in B.lists:
                    i.append(0)
            B.matrix = np.array(B.lists)
        C = self.matrix + B.matrix
        return C

    def minus(self, B):
        if len(self.matrix) < len(B.matrix):
            dif = len(B.matrix) - len(self.matrix)
            q = []
            for i in range(len(self.matrix[0])):
                q.append(0)
            for i in range(dif):
                self.lists.append(q)
            self.matrix = np.array(self.lists)
        if len(self.matrix) > len(B.matrix):
            dif = len(self.matrix) - len(B.matrix)
            q = []
            for i in range(len(B.matrix[0])):
                q.append(0)
            for i in range(dif):
                B.lists.append(q)
            B.matrix = np.array(B.lists)
        if len(self.matrix[0]) < len(B.matrix[0]):
            dif = len(B.matrix[0]) - len(self.matrix[0])
            for w in range(dif):
                for i in self.lists:
                    i.append(0)
            self.matrix = np.array(self.lists)
        if len(self.matrix[0]) > len(B.matrix[0]):
            dif = len(self.matrix[0]) - len(B.matrix[0])
            for w in range(dif):
                for i in B.lists:
                    i.append(0)
            B.matrix = np.array(B.lists)
        C = self.matrix - B.matrix
        return C

    def number_multiple(self, number):
        return self.matrix * number

    def multiple(self, B):
        if len(self.matrix[0]) != len(B.matrix):
            raise MatrixError('This matrices can not be multiplied')
        C = self.matrix.dot(B.matrix)
        return C

    def transponse(self):
        return self.matrix.transpose()


m1 = [[3, 4, 5]]

m2 = [[2, 7],
      [9, 7]]

m1 = Matrix(m1)
m2 = Matrix(m2)


print(m1.add(m2))
print(m2.minus(m1))
print(m1.number_multiple(2))
print(m1.multiple(m2))
print(m2.transponse())
