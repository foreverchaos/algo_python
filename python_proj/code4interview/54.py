"""
请实现一个函数用来找出字符流中第一个只出现一次的字符。例如，当从字符流中只读出前两个字符"go"时，
第一个只出现一次的字符是"g"。当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。
"""


class Solution:
    def __init__(self):
        self.s = ''
        self.count = {}

    def first_appearing_once(self):
        length = len(self.s)
        for i in range(length):
            if self.count[self.s[i]] == 1:
                return self.s[i]
        return '#'

    def insert(self, char):
        self.s += char
        self.count[char] = 1 if char not in self.count else self.count[char] + 1


if __name__ == '__main__':
    s = Solution()
    print(s.insert('g'))
    print(s.insert('o'))
    print(s.insert('o'))
    print(s.insert('o'))
    print(s.insert('g'))
    print(s.first_appearing_once())