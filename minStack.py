__author__ = 'cenk'

class MinStack:
    # initialize your data structure here.
    def __init__(self):
        self.stack = []
        self.minStack = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        if len(self.stack) == 0:
            self.stack.append(x)
            self.minStack.append(x)
        else:
            self.stack.append(x)
            if self.minStack[-1] < x:
                smallest = self.minStack[-1]
                self.minStack.append(smallest)
            elif self.minStack[-1] >= x:
                self.minStack.append(x)

    # @return nothing
    def pop(self):
        if len(self.stack) != 0:
            self.minStack.pop()
            return self.stack.pop()

    # @return an integer
    def top(self):
        if len(self.stack) != 0:
            return self.stack[-1]
        else:
            return -1

    # @return an integer
    def getMin(self):
        if len(self.stack) != 0:
            return self.minStack[-1]
        else:
            return -1

s = MinStack()
s.push(5)
s.push(1)
s.push(11)
s.push(20)

s.pop()
s.pop()
s.pop()
s.pop()

s.push(11)

print s.getMin()
print s.top()