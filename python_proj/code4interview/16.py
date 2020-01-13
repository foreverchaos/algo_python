"""
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def merge_linklist(pHead1, pHead2):
    if not pHead1 and not pHead2:
        return None
    i, j = pHead1, pHead2
    start = ListNode(0)
    temp = start
    while i and j:
        if i.val <= j.val:
            temp.next = i
            i = i.next
        else:
            temp.next = j
            j = j.next
        temp = temp.next
    temp.next = i or j
    return start.next


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.next = node4
    node4.next = node5
    node2.next = node3
    print(merge_linklist(node1, node2))