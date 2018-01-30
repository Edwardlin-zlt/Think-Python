def polyline(t, n, length, angle):
    """Draws n line segments.

    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    for i in range(n):
        fd(t, length)
        lt(t, angle)

def arc(t, r, angle):
    """Draws an arc with the given radius and angle.

    t: Turtle
    r: radius
    angle: angle subtended by the arc, in degrees
    """
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n

    # making a slight left turn before starting reduces
    # the error caused by the linear approximation of the arc
    lt(t, step_angle/2)
    polyline(t, n, step_length, step_angle)
    rt(t, step_angle/2)

def pedal(t,r,angle):
    '''draws a pedal with two arcs.

    t; Turtle
    r; radius of arcs
    angel;angle ( in degree) that subtends the arcs'''

    for i in range(2):
        arc(t,r,angle)
        lt(t,180-angle)

def flower(t,n,r,angle):
    '''Draws a flower with n pedals.

    t: Turtle
    n: number of pedals
    r;radius of arcs
    angle: angle (in degree)that subtends the arcs'''
    turn_angle = 360.0 / n
    for i in range(n):
        pedal(t,r,angle)
        lt(t,turn_angle)

def move(t,length):
    '''move turtle (t) forward (length) without leaving a trail.
    Then put down the pen'''
    pu(t)
    fd(t,length)
    pd(t)



import math
from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

# draw a sequence of three flowers, as shown in the book.
move(bob, -100)
flower(bob, 7, 60.0, 60.0)

move(bob, 100)
flower(bob, 10, 40.0, 80.0)

move(bob, 100)
flower(bob, 20, 140.0, 20.0)

die(bob)

# dump the contents of the campus to the file canvas.eps
world.canvas.dump()

wait_for_user()
