"""
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例 1:

输入: s = "anagram", t = "nagaram"
输出: true
"""

import string


def is_anagram(string_a, string_b):
    if len(string_a) != len(string_b):
        return False
    alpha_list = list(string.ascii_lowercase)
    new_dict = {alpha: 0 for alpha in alpha_list}

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


if __name__ == '__main__':
    print(is_anagram('anagram', 'nagaram'))