__author__ = 'cenk'


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l6 = ListNode(6)
l7 = ListNode(7)

l1.next = l2


def cycleNode(head):
    t1 = head
    t2 = head

    while t2 != None:
        t1= t1.next

        if t2.next == None:
            return None
        else:
            t2 = t2.next.next
        if t2 == t1:
            break

    tmp = head
    while tmp != None:
        if tmp == t1:
            return tmp
        if tmp == None or t1 == None:
            break
        tmp = tmp.next
        t1 = t1.next

    return None


t = cycleNode(l1)
print t.val
