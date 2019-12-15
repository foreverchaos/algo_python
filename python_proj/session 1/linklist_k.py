class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# def reverse_k_group(head: ListNode, k: int) -> ListNode:
#     cur = head
#     count = 0
#     while cur and count != k:
#         cur = cur.next
#         count += 1
#     if count == k:
#         cur = reverse_k_group(cur, k)
#         while count:
#             tmp = head.next
#             head.next = cur
#             cur = head
#             head = tmp
#             count -= 1
#         head = cur
#     return head

def reverse_k_group(head: ListNode, k: int) -> ListNode:
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
    results = reverse_k_group(list_node_1, 2)
    print(results.val)