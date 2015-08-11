__author__ = 'cenk'

class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

def maxPoints(points):
    if len(points) == 1:
        return 1

    dupDict = {}
    newPoints = []

    for i in points:
        iStr = str(i.x) + " " + str(i.y)
        if iStr not in dupDict:
            dupDict[iStr] = 0
            newPoints.append(i)
        else:
            dupDict[iStr] += 1

    if len(newPoints) == 1:
        iStr = str(newPoints[0].x) + " " + str(newPoints[0].y)
        return dupDict[iStr] + 1

    functions = {}
    for i in range(len(newPoints)):
        for k in range(i+1,len(newPoints)):
            func = findFunc(newPoints[i],newPoints[k])
            key = str(func) + str(i)
            if key not in functions:
                functions[key] = 2

                iStr = str(newPoints[i].x) + " " + str(newPoints[i].y)
                if iStr in dupDict:
                    functions[key] += dupDict[iStr]

                kStr = str(newPoints[k].x) + " " + str(newPoints[k].y)
                if kStr in dupDict:
                    functions[key] += dupDict[kStr]
            else:
                functions[key] += 1
                kStr = str(newPoints[k].x) + " " + str(newPoints[k].y)
                if kStr in dupDict:
                    functions[key] += dupDict[kStr]

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
# [[84,250],[0,0],[1,0],[0,-70],[0,-70],[1,-1],[21,10],[42,90],[-42,-230]]
# [[0,0],[1,1],[1,-1]]
# [[0,0],[-1,-1],[2,2]]
# print findFunc(p1,p2)
print maxPoints(points)
