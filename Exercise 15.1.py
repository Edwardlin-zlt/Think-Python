import math

class Point(object):
    """Represents a Point in 2-D space"""

def dis_bet_points(p1,p2):
    dx = p1.x - p2.x
    dy = p1.y - p2.y
    dis = math.sqrt(dx ** 2 + dy ** 2)
    return dis

if __name__ == '__main__':
    p1 = Point()
    p2 = Point()
    p1.x = 0
    p1.y = 0
    p2.x = 3
    p2.y = 4
    distance = dis_bet_points(p1, p2)
    print distance