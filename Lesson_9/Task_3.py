class Parallelogram:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def get_area(self):
        s = self.width * self.length
        return f"Площа паралелограма: {s}"


class Square(Parallelogram):
    def __init__(self, width):
        Parallelogram.__init__(self, width, length=None)
        self.width = width

    def get_area(self):
        s = self.width ** 2
        return f"Площа квадрату: {s}"


A = Parallelogram(10, 15)
B = Square(10)
print(A.get_area())
print(B.get_area())
