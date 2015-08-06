__author__ = 'cenk'


def simplifyPath(path):
    path = path.rstrip('/')
    dirs = path.split('/')
    stack = []
    for i in dirs:
        stack.append(i)

    lastDir = stack.pop()

    if "..." in lastDir:
        return "/" + lastDir
    elif "." in lastDir:
        return "/"
    else:
        return "/" + lastDir

a = "/..."
print simplifyPath(a)