class MyCar:
    def __int__(self, mark, color, volume_of_engine):
        self.mark = mark
        self.color = color
        self.volume_of_engine = volume_of_engine

    def forward(self):
        return 'Drive forward'

    def back(self):
        return 'Drive back'


class HisCar(MyCar):
    def __init__(self):
        MyCar.__init__(self)

    def right(self):
        return 'Turn right'

    def left(self):
        return 'Turn left'
