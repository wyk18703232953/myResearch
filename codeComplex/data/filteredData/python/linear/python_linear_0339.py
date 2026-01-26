import math

def main(n):
    if n <= 0:
        # print(0)
        pass
        return

    # 确定性生成 d
    d = 1 + (n % 5)

    # 确定性生成位置数组 pos，严格递增
    # 相邻差值在 1 到 2*d+2 之间变化，保证有多种情况
    pos = []
    cur = 0
    for i in range(n):
        diff = 1 + (i % (2 * d + 2))
        cur += diff
        pos.append(cur)

    count = 2
    for i in range(1, n):
        if math.fabs(pos[i] - pos[i - 1]) > 2 * d:
            count += 2
        elif math.fabs(pos[i] - pos[i - 1]) == 2 * d:
            count += 1

    # print(count)
    pass
if __name__ == "__main__":
    main(5)