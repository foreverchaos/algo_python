def reverse_sentence(s):
    res = s.split(" ")
    return ' '.join(res[::-1])


if __name__ == '__main__':
    string = 'student. a am I'
    print reverse_sentence(string)
