from bisect import bisect_left
import random

def main(n: int):
    # 1. 生成规模为 n 的测试数据 a，形式为 [(x1, y1), (x2, y2), ...]
    #    原题逻辑只要求 a 是可排序的整数对，这里随机生成：
    #    x 为 1..2n 的不重复整数，y 为 1..n 的正整数
    xs = list(range(1, 2 * n + 1))
    random.shuffle(xs)
    xs = xs[:n]
    ys = [random.randint(1, n) for _ in range(n)]
    a = list(zip(xs, ys))

    # 按原代码逻辑：对 a 排序
    a.sort()

    mem = [1]      # DP 数组
    pos = []       # 存储 x
    power = []     # 存储 y

    for x, y in a:
        pos.append(x)
        power.append(y)

    for i in range(1, n):
        ix = bisect_left(pos, pos[i] - power[i]) - 1
        if ix == -1:
            mem.append(1)
        else:
            mem.append(mem[ix] + 1)

    print(n - max(mem))


# 示例：直接运行时给一个默认规模
if __name__ == "__main__":
    main(10)