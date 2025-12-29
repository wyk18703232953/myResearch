from bisect import bisect_left
import random

def main(n):
    # 生成测试数据
    # n: 竖线数量
    # m: 横线相关的输入规模，设为 n 的同量级
    m = n

    # 竖直线位置：在 [1, 10^6] 中随机生成
    verticals = [random.randint(1, 10**6) for _ in range(n)]

    # h 中每个元素为 [t, val]
    # t 为 1 或 2，其中 t == 1 时才参与 horizontals
    h = []
    for _ in range(m):
        t = random.randint(1, 2)
        val = random.randint(1, 10**6)
        h.append([t, val])

    horizontals = [t[1] for t in h if t[0] == 1]

    verticals.sort()
    horizontals.sort()
    verticals.append(10**9)

    min_blockers = n + m
    for i, v in enumerate(verticals):
        cur_blockers = len(horizontals) - bisect_left(horizontals, v) + i
        if cur_blockers < min_blockers:
            min_blockers = cur_blockers

    print(min_blockers)


if __name__ == "__main__":
    # 举例：调用 main(10)，可根据需要修改规模
    main(10)