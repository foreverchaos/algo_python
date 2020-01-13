"""
根据每日 气温 列表，请重新生成一个列表，对应位置的输入是你需要再等待多久温度才会升高超过该日的天数。
如果之后都不会升高，请在该位置用 0 来代替。

例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。
"""


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