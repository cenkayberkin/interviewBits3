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

def rotateList(head,k):
    if head == None:
        return None

    lenght = 0
    tmp = head
    while tmp != None:
        lenght += 1
        tmp = tmp.next

    k = k % lenght
    if k == 0:
        return head

    index = lenght - k - 1

    tmp = head
    i = 0
    while i < index:
        i += 1
        tmp = tmp.next

    newHead = tmp.next

    tmp.next = None
    newtmp = newHead

    while newtmp.next != None:
        newtmp = newtmp.next

    newtmp.next = head
    return newHead

t = rotateList(l1,2)

tmp = t
while tmp != None:
    print tmp.val
    tmp = tmp.next


