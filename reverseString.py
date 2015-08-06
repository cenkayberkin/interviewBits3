__author__ = 'cenk'

def reverseString(A):
    stack = []
    for i in A:
        stack.append(i)
    result = ""

    while len(stack) > 0:
        result += stack.pop()
    return result

a = "abc"
print reverseString(a)
