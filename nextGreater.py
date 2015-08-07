__author__ = 'cenk'

# Function to replace every element with the
#   next greatest element
def nextGreater(arr):
    i = 0
    stack = []
    element = 0
    next = 0
    result = []
    stack.append(arr[0])

    for i in range(len(arr)):
        next = arr[i]

        if len(stack) != 0:
            element = stack.pop()

            while element < next:
                result.append(next)
                if len(stack) == 0:
                    break
                element = stack.pop()

            if element > next:
                stack.append(element)

        stack.append(next)

    while len(stack) != 0:
        element = stack.pop()
        next = -1
        result.append(next)
    return result



a= [4,5,2,10]
r = nextGreater(a)
print r