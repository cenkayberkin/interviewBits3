__author__ = 'cenk'

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

l1 = ListNode(3)
l2 = ListNode(7)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l6 = ListNode(6)
l7 = ListNode(7)
l8 = ListNode(8)




def substract(head):

    length = 0

    tmp = head
    while tmp != None:
        length += 1
        tmp = tmp.next

    if length == 1:
        return head
    if length == 2:
        head.val = head.next.val - head.val
        return head

    start = 0
    if length % 2 == 0:
        start = (length / 2)
    else:
        start = (length / 2) + 1

    i  = 1
    firstLast = head
    while i < start:
        i+= 1
        firstLast = firstLast.next

    secondHead = firstLast.next
    firstLast.next = None
    secondHead = reverseList(secondHead)

    f = head
    s = secondHead
    while f != None and s != None:
        f.val = s.val - f.val
        f = f.next
        s = s.next

    secondHead = reverseList(secondHead)
    firstLast.next = secondHead
    return head

def reverseList(head):
    newList = None
    tmp = head.next
    cur = head
    while cur != None:
        cur.next = newList
        newList = cur
        cur = tmp
        if tmp != None:
            tmp = tmp.next
    return newList

h = substract(l1)
t = h

while t != None:
    print t.val
    t = t.next




