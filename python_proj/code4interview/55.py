class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def entry_node_of_loop(pHead):
    # res = []
    # temp = ListNode(0)
    # temp.next = pHead
    # while temp.next:
    #     temp = temp.next
    #     if temp in res:
    #         return temp
    #     res.append(temp)
    # if not res:
    #     return None
    head = ListNode(0)
    head.next = pHead
    fast = head
    slow = head
    while True:
        if fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        else:
            return None
        if fast == slow:
            fast = head
            break
    while fast != slow:
        fast = fast.next
        slow = slow.next
    return fast


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)
    node7 = ListNode(7)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node1
    # node6.next = node7
    # node7.next = node3
    print entry_node_of_loop(node1).val