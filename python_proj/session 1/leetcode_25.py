"""
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。

如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

示例 :

给定这个链表：1->2->3->4->5

当 k = 2 时，应当返回: 2->1->4->3->5

当 k = 3 时，应当返回: 3->2->1->4->5
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverse_k_group(head, k):
    prev = None
    curr = head
    n = k
    count = 0
    end = curr
    while end and count != k:
        end = end.next
        count = count + 1
    if count == k:
        while curr and n > 0:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            n = n - 1
        head.next = reverse_k_group(curr, k)
    else:
        prev = curr
    return prev


if __name__ == '__main__':
    list_node_1 = ListNode(1)
    list_node_2 = ListNode(2)
    list_node_3 = ListNode(3)
    list_node_4 = ListNode(4)
    list_node_5 = ListNode(5)
    list_node_6 = ListNode(6)
    list_node_1.next = list_node_2
    list_node_2.next = list_node_3
    list_node_3.next = list_node_4
    list_node_4.next = list_node_5
    list_node_5.next = list_node_6
    results = reverse_k_group(list_node_1, 3)
    print(results)