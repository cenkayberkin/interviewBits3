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
l2.next = l3
l3.next = l4
l4.next = l5
l5.next = l6
l6.next = l7

def reverseBetween(head, m, n):
    if head.next == None:
        return head


    i = 1
    lastNodeUnReversed = head

    while i < m -1:
        i += 1
        lastNodeUnReversed = lastNodeUnReversed.next

    reverseHead = lastNodeUnReversed.next
    reverseTail = head

    i = 1
    while i < n:
        i += 1
        reverseTail = reverseTail.next

    secondHeadUnReversed = reverseTail.next
    reverseTail.next = None

    if m == 1:
        newTmp = ListNode(-1)
        newTmp.next = head
        reverseHead,reverseTail = reverseLinkedList(head)
        reverseTail.next = secondHeadUnReversed
        return reverseHead

    lastNodeUnReversed.next = None

    reverseHead,reverseTail = reverseLinkedList(reverseHead)

    lastNodeUnReversed.next = reverseHead
    reverseTail.next = secondHeadUnReversed

    return head

def reverseLinkedList(head):
    newHead = None
    newTail = head

    tmp = head
    holder = tmp.next

    while tmp != None:
        tmp.next = newHead
        newHead = tmp
        tmp = holder
        if holder != None:
            holder = holder.next
    return newHead,newTail

t = reverseBetween(l1,1,7)

tmp = t
while tmp != None:
    print tmp.val
    tmp = tmp.next