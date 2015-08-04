__author__ = 'cenk'


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(2)
l4 = ListNode(4)
l5 = ListNode(5)
l6 = ListNode(5)

l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
l5.next = l6

def deleteDuplicates(head):
    if head == None:
        return None
    s = set()

    tmp = head
    s.add(tmp.val)
    while tmp.next != None:
        if tmp.next.val in s:
            tmp.next = tmp.next.next
        else:
            s.add(tmp.next.val)
            tmp = tmp.next
    return head

t = deleteDuplicates(l1)

tmp = t
while tmp != None:
    print tmp.val
    tmp = tmp.next