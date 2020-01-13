"""
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。
例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def delete_duplication(pHead):
    if not pHead:
        return None
    start = ListNode(None)
    start.next = pHead
    prev = start
    curr = pHead
    while curr.next:
        next = curr.next
        if next.val == curr.val:
            while next and next.val == curr.val:
                curr = next
                next = next.next
            if not next:
                prev.next = None
                return start.next
            prev.next = next
            curr = next
        else:
            prev = curr
            curr = curr.next
    return start.next


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(1)
    node3 = ListNode(2)
    node4 = ListNode(3)
    node5 = ListNode(3)
    node6 = ListNode(4)
    node7 = ListNode(5)
    node8 = ListNode(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    node7.next = node8
    print(delete_duplication(node1))