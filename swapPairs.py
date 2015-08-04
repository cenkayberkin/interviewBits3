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


l1.next = l2




def swapPairs(head):
    if head == None:
        return None

    first = head
    second = head.next

    if second == None:
        return first

    holder= None
    resultH = None
    resultT = None

    while second != None:
        if resultH == None:
            holder = second.next
            resultH = second
            first.next = None
            resultT = first

            resultH.next = resultT


        else:
            holder = second.next
            resultT.next = second
            resultT = resultT.next
            first.next = None
            resultT.next = first
            resultT = resultT.next

        first = holder
        if holder == None:
            break
        elif holder.next == None:
            holder.next = None
            resultT.next = holder
            resultT = resultT.next
            break
        else:
            second = holder.next

    return resultH

t = swapPairs(l1)

tmp = t
while tmp != None:
    print tmp.val
    tmp = tmp.next
