# Yihan Xiao 2018/09/27
class Position(object):
    '''Position is a pair of coordinates (x,y)'''
    def __init__(self, x, y):
        assert type(x) == int
        assert type(y) == int
        self.x = x
        self.y = y

    def __add__(self, other):
        assert type(other) == Position
        return Position(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        assert type(other) == Position
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def __str__(self):
        return str(self.x) + ' ' + str(self.y)

 

