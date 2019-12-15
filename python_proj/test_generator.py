import string


def reverse_string(input_str):
    if not isinstance(input_str, str):
        return Exception('not string')
    else:
        new_list = list(input_str)
        i, j = 0, len(new_list) - 1
        while i < j:
            new_list[i], new_list[j] = new_list[j], new_list[i]
            i += 1
            j -= 1
        return ''.join(new_list)


def is_anagram(string_a, string_b):
    if len(string_a) != len(string_b):
        return False
    alpha_list = list(string.ascii_lowercase)
    new_dict = {}
    for alpha in alpha_list:
        new_dict[alpha] = 0

    for item in string_a:
        if item in new_dict.keys():
            new_dict[item] += 1

    for item in string_b:
        if item in new_dict.keys():
            new_dict[item] -= 1

    for value in new_dict.values():
        if value != 0:
            return False
    return True


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverse_k_group(head: ListNode, k: int) -> ListNode:
    cur = head
    count = 0
    while cur and count != k:
        cur = cur.next
        count += 1
    if count == k:
        cur = reverse_k_group(cur, k)
        while count:
            tmp = head.next
            head.next = cur
            cur = head
            head = tmp
            count -= 1
        head = cur
    return head


if __name__ == '__main__':
    # print(reverse_string('algorithm'))
    # print(is_anagram('anagram', 'nagaram'))
    list_node_1 = ListNode(1)
    list_node_2 = ListNode(2)
    list_node_3 = ListNode(3)
    list_node_4 = ListNode(4)
    list_node_5 = ListNode(5)
    list_node_1.next = list_node_2
    list_node_2.next = list_node_3
    list_node_3.next = list_node_4
    list_node_4.next = list_node_5
    results = reverse_k_group(list_node_1, 2)
    1, 2, 3, 4, 5