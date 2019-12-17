
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def find_first_common_node(pHead1, pHead2):
    # write code here
    if pHead1 == None or pHead2 == None:
        return None
    cur1, cur2 = pHead1, pHead2
    while cur1 != cur2:
        cur1 = cur1.next if cur1 != None else pHead2
        cur2 = cur2.next if cur2 != None else pHead1
    return cur1


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)
    node7 = ListNode(7)

    node1.next = node7
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7

    print find_first_common_node(node1, node2)
