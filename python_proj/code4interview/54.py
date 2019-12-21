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
        if char not in self.count:
            self.count[char] = 1
        else:
            self.count[char] += 1


if __name__ == '__main__':
    s = Solution()
    print(s.insert('g'))
    print(s.insert('o'))
    print(s.insert('o'))
    print(s.insert('o'))
    print(s.insert('g'))
    print s.first_appearing_once()