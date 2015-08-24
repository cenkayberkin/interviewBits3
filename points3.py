__author__ = 'cenk'
from collections import defaultdict

class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

def maxPoints(X,Y):
    # test = defaultdict(list)
    if len(X) == 1:
        return 1
    dict = defaultdict(int)
    result = 0
    for i in range(len(X)):
        j = i
        dup = 1
        dict.clear()
        tmpResult = 0
        while j < len(X):
            if i != j:
                if X[i] == X[j] and Y[i] == Y[j]:
                    dup += 1
                elif X[i] == X[j]:
                    dict['x'] += 1
                elif Y[i] == Y[j]:
                    dict['y'] += 1
                else:
                    m = float(Y[i] - Y[j]) / (X[i] - X[j])
                    a = Y[i] - (m * X[i])
                    #  y - mx = a
                    dict[(m,a)] += 1
                    # test[(m,a)].append((i,j))

            j += 1

        if len(dict.values()) > 0:
            tmpResult = max(dict.values())

        tmpResult += dup
        result = max(result,tmpResult)


    return result

# [[84,250],[0,0],[1,0],[0,-70],[0,-70],[1,-1],[21,10],[42,90],[-42,-230]]
#  y = 2x + 82
x = [84,0,1,0,0,1,21,42,-42]
y = [250,0,0,-70,-70,-1,10,90,-230]

# p1 = Point(84,250)
# p2 = Point(0,0)
# p3 = Point(1,0)
# p4 = Point(0,-70)
# p5 = Point(0,-70)
# p6 = Point(1,-1)
# p7 = Point(21,10)
# p8 = Point(42,90)
# p9 = Point(-42,-230)

# points = [p1,p2,p3,p4,p5,p6,p7,p8,p9]
print maxPoints(x,y)