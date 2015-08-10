__author__ = 'cenk'

class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

def maxPoints(points):
    if len(points) == 1:
        return 1
    functions = {}
    for i in range(len(points)):
        for k in range(i+1,len(points)):
            func = findFunc(points[i],points[k])
            key = str(func) + str(i)
            if key not in functions:
               functions[key] = 2

            else:
                functions[key] += 1

    max = 0
    for i in functions.values():
        if i > max:
            max = i

    return max


# finds function of line which passes from p1 and p2
# y = ax + b => function returns (a,b)
def findFunc(p1,p2):
    if p1.x == p2.x and p1.y == p2.y:
        return (p1.x,p1.y,p2.x,p2.y)
    elif p1.x == p2.x:
        return ('x',p1.x,p2.x)
    elif p1.y == p2.y:
        return ('y',p1.y,p2.y)

    yDiff = p2.y - p1.y
    xDiff = p2.x - p1.x

    if xDiff != 0:
        a =  yDiff / xDiff
    else:
        a = 1

    b = p1.y - (a * p1.x)
    return a,b

p1 = Point(0,0)
p2 = Point(-1,-1)
p3 = Point(2,2)
p4 = Point(0,0)
p5 = Point(0,5)
p6 = Point(1,9)
p7 = Point(1,10)
p8 = Point(1,12)
points = [p1,p2,p3]
# [[0,0],[1,1],[1,-1]]
# [[0,0],[-1,-1],[2,2]]
# print findFunc(p1,p2)
print maxPoints(points)
