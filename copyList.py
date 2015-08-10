__author__ = 'cenk'


class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

l1 = RandomListNode(-1)
l2 = RandomListNode(5)
l3 = RandomListNode(10)
l4 = RandomListNode(15)
l5 = RandomListNode(20)
l6 = RandomListNode(25)

# l1.next = l2
l1.random = None
# l2.next = l3
# l2.random = l1
# l3.next = l4
# l3.random = l6
# l4.next = l5
# l4.random = l4
# l5.next = l6
# l5.random = l1
# l6.random = l2

def copyRandomList(head):
    if head == None or head.label == None:
        return None


    dict = {}
    t = head.next

    newHead = RandomListNode(head.label)
    newHead.random = head.random
    newTail = newHead
    dict[head] = newHead

    newNode = None

    while t != None:
        newNode = RandomListNode(t.label)
        newNode.random = t.random
        dict[t] = newNode
        newTail.next  = newNode
        newTail = newTail.next
        t = t.next

    s = newHead
    while s != None:
        if s.random != None:
            s.random = dict[s.random]
        else:
            s.random = None
        s =  s.next
    return newHead

t = copyRandomList(l1)

tmp = t
while tmp != None:
    print tmp.label
    if tmp.random != None:
        print " " + str(tmp.random.label)
    else:
        print " None "
    tmp = tmp.next