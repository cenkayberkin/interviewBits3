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


def reOrder(head):
    lenght = findLength(head)
    halfIndex = 0

    if lenght % 2 == 0:
        halfIndex = (lenght / 2)
    else:
        halfIndex  = (lenght / 2) + 1

    tmp = head
    i = 1
    while i < halfIndex:
        i += 1
        tmp = tmp.next

    halfH = tmp.next
    tmp.next = None

    halfH = reverse(halfH)
#     now merge head and halfH
    halfTmp = halfH
    headTmp = head

    resultH = headTmp
    resultT = halfTmp

    resultH.next = resultT
    resultT.next = None

    headTmp = headTmp.next
    halfTmp = halfTmp.next

    while halfTmp != None or headTmp != None:
        if halfTmp == None:
            resultT.next = headTmp
            resultT = resultT.next
            headTmp = headTmp.next
        elif headTmp == None:
            resultT.next = halfTmp
            resultT = resultT.next
            halfTmp = halfTmp.next
        else:
            resultT.next = headTmp
            resultT = resultT.next
            resultT.next = halfTmp
            resultT = resultT.next
            headTmp = headTmp.next
            halfTmp = halfTmp.next

    return resultH

def reverse(head):
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

def findLength(head):
    tmp = head
    result = 0
    while tmp != None:
        result += 1
        tmp = tmp.next
    return result

tmp = reOrder(l1)

while tmp != None:
    print tmp.val
    tmp = tmp.next