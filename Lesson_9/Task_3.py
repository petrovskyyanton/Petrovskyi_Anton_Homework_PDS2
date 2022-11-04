class Parallelogram:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def get_area(self):
        s = self.width * self.length
        return f"Площа паралелограма: {s}"


class Square(Parallelogram):
    def __init__(self, width, length):
        Parallelogram.__init__(self, width, length)
        self.width = width

    def get_area(self):
        s = self.width ** 2
        return f"Площа квадрату: {s}"
