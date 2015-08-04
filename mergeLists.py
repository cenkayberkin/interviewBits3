__author__ = 'cenk'


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

l1 = ListNode(1)
l2 = ListNode(5)
l3 = ListNode(10)
l4 = ListNode(15)
l5 = ListNode(20)
l6 = ListNode(25)

l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
l5.next = l6

l11 = ListNode(3)
l22 = ListNode(7)
l33 = ListNode(16)
l44 = ListNode(23)

l11.next = l22
l22.next = l33
l33.next = l44

def mergeTwoLists(l1, l2):
    if l1 == None:
        return l2
    elif l2 == None:
        return l1

    resultH = None
    resultT = None

    tmp1 = l1
    tmp2 = l2

    while tmp1 != None or tmp2 != None:
        if tmp1 == None:
            resultH,resultT = addNode(resultH,resultT,tmp2)
            tmp2 = tmp2.next
        elif tmp2 == None:
            resultH,resultT = addNode(resultH,resultT,tmp1)
            tmp1 = tmp1.next
        elif tmp1.val >= tmp2.val:
            resultH,resultT = addNode(resultH,resultT,tmp2)
            tmp2 = tmp2.next
        elif tmp2 == None or tmp1.val < tmp2.val:
            resultH,resultT = addNode(resultH,resultT,tmp1)
            tmp1 = tmp1.next

    return resultH

def addNode(resultH,resultT,newNode):
    if resultH == None:
        resultH = newNode
        resultT = newNode
    else:
        resultT.next = newNode
        resultT = resultT.next
    return resultH,resultT

t = mergeTwoLists(l1,l11)

tmp = t
while tmp != None:
    print tmp.val
    tmp = tmp.next