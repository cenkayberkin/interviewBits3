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

l1.next = l2
l2.next = l3
l3.next = l4

l4.next = l5
l5.next = l6

l11 = ListNode(11)
l12 = ListNode(12)
l13 = ListNode(13)
l14 = ListNode(14)
l15 = ListNode(15)
l16 = ListNode(16)

l11.next = l12
l12.next = l13
l13.next = l14
l14.next = l15
l15.next = l16
l16.next = l4


def getIntersectionNode(A, B):
    length1 = 0
    length2 = 0
    tmpA = A
    tmpB = B

    while tmpA != None:
        tmpA = tmpA.next
        length1 += 1

    while tmpB != None:
        tmpB = tmpB.next
        length2 += 1

    largerListHead = A
    smallerListHead = B

    steps = 0
    if length2 < length1:
        largerListHead  = A
        smallerListHead = B
        steps = length1 - length2
    elif length2 > length1:
        largerListHead  = B
        smallerListHead = A
        steps = length2 - length1

    if largerListHead != None:
        i = 0
        while i < steps:
            largerListHead = largerListHead.next
            i += 1
    while largerListHead != None and smallerListHead != None:
        if largerListHead == smallerListHead:
            return largerListHead
        largerListHead = largerListHead.next
        smallerListHead = smallerListHead.next
    return None

print getIntersectionNode(l1,l11)