"""
“student. a am I”。后来才意识到，这家伙原来把句子单词的顺序翻转了，正确的句子应该是“I am a student.”
"""


def reverse_sentence(s):
    res = s.split(" ")
    return ' '.join(res[::-1])


if __name__ == '__main__':
    string = 'student. a am I'
    print(reverse_sentence(string))
