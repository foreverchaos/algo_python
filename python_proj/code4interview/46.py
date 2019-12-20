class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def last_remaining(n, m):
    chain = [ListNode(i) for i in range(n)]
    for i in range(len(chain) - 1):
        chain[i].next = chain[i+1]
    chain[n-1].next = chain[0]
    curr = chain[0]
    prev = None

    while True:
        i = 0
        while i < m - 1:
            prev = curr
            curr = curr.next
            i += 1
        if curr == curr.next.next:
            return curr.next.val
        prev.next = curr.next
        curr = curr.next


if __name__ == '__main__':
    print last_remaining(10, 4)
