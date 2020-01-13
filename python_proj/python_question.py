# vim: set fileencoding=utf-8 :
from collections import defaultdict
import random

# usage of defaultdict
a = ["a", "b", "a"]
b = [10, 11, 12]
d = {}
new_d = zip(a, b)
print dict(new_d)

d = defaultdict(str)
for index, i in enumerate(a):
    d[i] += str(b[index])
print d
print d["c"]

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)

print dict(d)


arr = [1, 2, 3, 4, 5]
arr2 = map(lambda x: x**2, arr)
print arr2

print [x for x in arr2 if x > 10]


s = "ajldjlajfdljfddd"

print ''.join(sorted(set(s)))

dic = {"name": "zs", "age": 18, "city": "深圳", "tel": "1362626627"}
print dict(sorted(dic.items(), key=lambda i: i[0]))

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print filter(lambda x: x % 2 != 0, a)
print [n for n in a if n % 2 != 0]

array = [[1, 2], [3, 4], [5, 6]]
print [x for j in array for x in j]

x, y, z = 'abc', 'def', ['d', 'e', 'f']
print x.join(y)
print x.join(z)


test_a = ['a', 'b', False]
print any(test_a)
print all(test_a)


print random.random()

temp_array = '1982376455'
res2 = sorted(temp_array, key=lambda x: int(x) % 2 == 0 and 20 - int(x) or int(x))
print res2

# and， 从左到右扫描，返回第一个为假的表达式值，无假值则返回最后一个表达式值。
# or, 从左到右扫描，返回第一个为真的表达式值，无真值则返回最后一个表达式值。

# def multi():
#     return [lambda x : i*x for i in range(4)]


def multi():
    res =[]
    def inner(x):
        return i * x
    for i in range(4):
        res.append(inner)

    return res


a = multi()[0](3)
print a

# temp_arr = [m(3) for m in multi()]
# print temp_arr
x = 2
print map(lambda x:x**2, [y for y in range(3)])

dogdistance = {'dog-dog': 33, 'dog-cat': 36, 'dog-car': 41, 'dog-bird': 42}

min(dogdistance, key=dogdistance.get)
max(dogdistance, key=dogdistance.get)