class Solution:
    def __init__(self):
        self.data = []

    def get_median(self):
        length = len(self.data)
        if length % 2 == 0:
            return (self.data[length/2-1] + self.data[length/2])/2.0
        else:
            return self.data[length/2]

    def insert(self, num):
        if self.data:
            for i in range(len(self.data) - 1, -1, -1):
                if num > self.data[i]:
                    self.data.insert(i + 1, num)
                    return
            self.data.insert(0, num)
        else:
            self.data.append(num)


if __name__ == '__main__':
    s = Solution()
    s.insert(5)
    print s.get_median()
    s.insert(2)
    print s.get_median()
    s.insert(3)
    print s.get_median()
    s.insert(4)
    print s.get_median()
    s.insert(1)
    print s.get_median()
