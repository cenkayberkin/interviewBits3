__author__ = 'cenk'

def getMaxArea(hist):
    max = 0
    stack = []
    i = 0

    while i < len(hist):
        if len(stack) == 0 or hist[stack[-1]] <= hist[i]:
            stack.append(i)
            i += 1
        else:
            tp = stack[-1]
            stack.pop()
            right = 0
            if len(stack) == 0:
                right = i
            else:
                right = i - stack[-1] - 1

            area_with_top = hist[tp] * right
            if max < area_with_top:
                max = area_with_top

    while len(stack) != 0:
        tp = stack[-1]
        stack.pop()

        right = 0
        if len(stack) == 0:
            right = i
        else:
            right = i - stack[-1] - 1

        area_with_top = hist[tp] * right

        if max < area_with_top:
            max = area_with_top

    return max

a = [2,1,5,6,2,3]
print getMaxArea(a)
