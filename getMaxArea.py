__author__ = 'cenk'

def getMaxArea2(height):
    height.append(0)
    s = []
    i=0
    maxSize=0
    while i != len(height):
        if len(s) == 0 or height[i] >= height[s[-1]]:
            s.append(i)
            i += 1
        else:
            j = height[s[-1]]
            s.pop()
            bottom = 0
            if len(s) == 0:
                bottom = i
            else:
                bottom = i - s[-1] - 1

            area_with_top = j * bottom
            if maxSize < area_with_top:
                maxSize = area_with_top

    height.pop()
    return maxSize


# def getMaxArea(hist):
#     max = 0
#     stack = []
#     i = 0
#
#     while i < len(hist):
#         if len(stack) == 0 or hist[stack[-1]] <= hist[i]:
#             stack.append(i)
#             i += 1
#         else:
#             tp = stack[-1]
#             stack.pop()
#             right = 0
#             if len(stack) == 0:
#                 right = i
#             else:
#                 right = i - stack[-1] - 1
#
#             area_with_top = hist[tp] * right
#             if max < area_with_top:
#                 max = area_with_top
#
#     while len(stack) != 0:
#         tp = stack[-1]
#         stack.pop()
#
#         right = 0
#         if len(stack) == 0:
#             right = i
#         else:
#             right = i - stack[-1] - 1
#
#         area_with_top = hist[tp] * right
#
#         if max < area_with_top:
#             max = area_with_top
#
#     return max

# a = [4 ,1000 ,1000 ,1000 ,1000]
# a= [7,2, 1, 4, 5, 1, 3, 3]
# a = [2,1,5,6,2,3]
# a = [6, 2, 5, 4, 5, 1, 6]

def getMax3(heights):
    heights.append(0)
    i = 0
    stack = []
    max = 0
    while i < len(heights):
        if len(stack) == 0 or heights[stack[-1]] <= heights[i]:
            stack.append(i)
            i += 1
        else:
            tp = stack[-1]
            stack.pop()
            base = 0
            if len(stack) == 0:
                base = i
            else:
                base = i - stack[-1] - 1

            newRect = heights[tp] * base
            if max < newRect:
                max = newRect
    heights.pop()
    return max


a = [2,1,5,6,2,3]
# a = [1,1,2,1,3,1,5]
print getMax3(a)
