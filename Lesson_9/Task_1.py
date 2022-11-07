class MyCar:
    def __init__(self, mark, color, volume_of_engine):
        self.mark = mark
        self.color = color
        self.volume_of_engine = volume_of_engine

    def forward(self):
        return f'{self.color} {self.mark} moves forward'

    def back(self):
        return f'{self.color} {self.mark} moves back'


class HisCar(MyCar):
    def __init__(self, mark, color, volume_of_engine):
        MyCar.__init__(self, mark, color, volume_of_engine)

    def right(self):
        return f'{self.color} {self.mark} turns right'

    def left(self):
        return f'{self.color} {self.mark} turns left'


audi = MyCar('Audi', 'blue', 45)
bmw = HisCar('BMW', 'black', 50)
print(audi.forward())
print(audi.back())
print(bmw.forward())
print(bmw.back())
print(bmw.right())
print(bmw.left())
