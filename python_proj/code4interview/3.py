class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def print_tail_to_head(list_node, res):
    if list_node:
        print_tail_to_head(list_node.next)
        res.append(list_node.val)
    return res
