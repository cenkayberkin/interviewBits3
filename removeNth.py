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

def removeNth(head,n):
    if head == None:
        return None

    tmp1 = head
    tmp2 = head

    i = 0
    while i < n and tmp1 != None:
        i += 1
        tmp1 = tmp1.next

    if tmp1 != None:
        while tmp1.next != None:
            tmp1 = tmp1.next
            tmp2 = tmp2.next
    else:
        head = head.next
        return head

    tmp2.next = tmp2.next.next

    return head

t = removeNth(l1,11)

tmp = t
while tmp != None:
    print tmp.val
    tmp = tmp.next