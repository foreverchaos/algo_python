def count_and_say(n):
    if n == 1:
        return '1'

    prev = count_and_say(n-1)
    string = ''
    temp = []
    for item in prev:
        if not temp or item in temp:
            temp.append(item)
        else:
            string += str(len(temp)) + temp[0]
            temp = [item]
    string += str(len(temp)) + temp[0]
    return string


if __name__ == '__main__':
    print count_and_say(10)
