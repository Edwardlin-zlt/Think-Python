class Point():

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "( %d, %d)" %(self.x, self.y)

    def __add__(self, other):
        if isinstance(other,Point):
            x = self.x + other.x
            y = self.y + other.y
            return Point(x, y)
        elif isinstance(other, tuple):
            x = self.x + other[0]
            y = self.y + other[1]
            return Point(x, y)

    def __radd__(self, other):
        if isinstance(other, tuple):
            x = self.x + other[0]
            y = self.y + other[1]
            return Point(x, y)

if __name__ == '__main__':
    p1 = Point(3, 4)
    p2 = Point(2, 1)
    p3 = (3, 4)
    print p1 + p2
    print p3 + p1