class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Pawn:
    def __init__(self, position, color):
        self.__position = position
        self.__color = color
        pass
