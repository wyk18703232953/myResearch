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
    # 生成长度为 n 的整数列表，含正数和负数，结构完全由 n 决定
    # 元素定义为：(-1)**i * (i % 7 + 1)
    slimes = [((-1) ** i) * (i % 7 + 1) for i in range(n)]
    res = solve(slimes)
    # 保持与原程序相同的输出行为：输出单个结果
    # print(res)
    pass
if __name__ == "__main__":
    # 示例调用：可按需修改 n 的值做实验
    main(10)