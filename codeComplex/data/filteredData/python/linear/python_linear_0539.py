def solve(slimes):
    if len(slimes) == 1:
        return slimes[0]

    havePos = False
    haveNeg = False

    for s in slimes:
        if s > 0:
            havePos = True
        elif s < 0:
            haveNeg = True

    if havePos and haveNeg:
        return sum(map(abs, slimes))
    elif not havePos:
        m = max(slimes)
        return sum(list(map(abs, slimes))) + 2 * m
    elif not haveNeg:
        m = min(slimes)
        return sum(list(map(abs, slimes))) - 2 * m

    else:
        return 0


def main(n):
    # 生成长度为 n 的整数列表，包含正数、负数和零，构造完全确定
    # 示例: [0, 1, -1, 2, -2, 3, -3, ...]
    slimes = []
    for i in range(n):
        if i % 3 == 0:
            val = 0
        elif i % 3 == 1:
            val = i // 3 + 1

        else:
            val = -(i // 3 + 1)
        slimes.append(val)
    result = solve(slimes)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)