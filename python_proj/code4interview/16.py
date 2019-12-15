
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def merge_linklist(pHead1, pHead2):
    if not pHead1 and not pHead2:
        return None
    if pHead1 and not pHead2:
        return pHead1
    elif not pHead1 and pHead2:
        return pHead2
    i, j = pHead1, pHead2
    if pHead1.val <= pHead2.val:
        new_head = pHead1
        i = pHead1.next
        new_head.next = None

    temp = new_head
    while i and j:
        if i.val <= j.val:
            temp.next = i
            i = i.next
        else:
            temp.next = j
            j = j.next
        temp = temp.next
    if i:
        temp.next = i
    if j:
        temp.next = j
    return new_head


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.next = node4
    node4.next = node5
    node2.next = node3
    print merge_linklist(node1, node2)