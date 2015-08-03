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

def reverseList(head):
    if head.next  == None:
        return head

    prev = reverseList(head.next)
    head.next = None
    prev.next = head

    return head

reverseList(l1)

tmp = l6

while tmp != None:
    print tmp.val
    tmp = tmp.next
