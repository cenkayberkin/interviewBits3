__author__ = 'cenk'


class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

def maxPoints(points):
    pass




p1 = Point(84,250)
p2 = Point(0,0)
p3 = Point(1,0)
p4 = Point(0,-70)
p5 = Point(0,-70)
p6 = Point(1,-1)
p7 = Point(21,10)
p8 = Point(42,90)
p9 = Point(-42,-230)

points = [p1,p2,p3,p4,p5,p6,p7,p8,p9]
print maxPoints(points)
