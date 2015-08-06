__author__ = 'cenk'

def isValid(s):
    stack = []
    left = "[{("
    right = "])}"

    for i in s:
        if len(stack) == 0 and i in right:
            return False
        if i in left:
            stack.append(i)
        elif i in right:
            top = stack.pop()
            if i == ")" and top == "(":
                continue
            elif i == "]" and top == "[":
                continue
            elif i == "}" and top == "{":
                continue
            else:
                return False

    if len(stack) == 0:
        return True
    else:
        return False

a = "["
print isValid(a)