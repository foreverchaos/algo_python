
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 快慢指针
def find_kth_to_tail(head, k):
    if not head:
        return None
    pos_k = head
    pos_start = head
    for i in range(k-1):
        if pos_k.next:
            pos_k = pos_k.next
        else:
            return pos_k

    while pos_k.next:
        pos_k = pos_k.next
        pos_start = pos_start.next
    return pos_start.val


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    print find_kth_to_tail(node1, 5)