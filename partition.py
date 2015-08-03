__author__ = 'cenk'

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

l1 = ListNode(111)
l2 = ListNode(222)
l3 = ListNode(3)
l4 = ListNode(8)
l5 = ListNode(15)
l6 = ListNode(22)

l1.next = l2


def partition(head,k):
    if head == None:
        return None

    lessL = None
    lessH = None
    moreL = None
    moreH = None
    tmp = head.next
    cur = head

    while cur != None:
        if cur.val < k:
            if lessH == None:
                cur.next = None
                lessH = cur
                lessL = cur
            else:
                cur.next = None
                lessL.next = cur
                lessL = lessL.next
        else:
            if moreH == None:
                cur.next = None
                moreH = cur
                moreL = cur
            else:
                cur.next = None
                moreL.next = cur
                moreL = moreL.next
        cur = tmp
        if tmp != None:
            tmp = tmp.next

    result = None
    if lessL != None:
        lessL.next = moreH
        result = lessH
    else:
        result = moreH

    return result


t = partition(l1,16)

tmp = t
while tmp != None:
    print tmp.val
    tmp = tmp.next

