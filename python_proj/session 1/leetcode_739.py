def daily_temperatures(temp_list):
    stacks = []
    up_list = [0]*len(temp_list)
    for idx, value in enumerate(temp_list):
        while stacks and value > temp_list[stacks[-1]]:
            up_list[stacks[-1]] = idx - stacks[-1]
            stacks.pop()
        stacks.append(idx)
    return up_list


if __name__ == '__main__':
    results = daily_temperatures([23, 25, 21, 19, 22, 26, 23])
    print(results)