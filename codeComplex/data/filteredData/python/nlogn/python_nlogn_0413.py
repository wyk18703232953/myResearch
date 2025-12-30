from collections import defaultdict
import random

def main(n: int):
    # 生成测试数据：n 个区间 [a, b]
    # 这里示例生成：0 <= a <= b <= 2n
    intervals = []
    for _ in range(n):
        a = random.randint(0, 2 * n)
        b = random.randint(a, 2 * n)
        intervals.append((a, b))

    ans = defaultdict(int)

    beg, end = [0] * n, [0] * n
    for i in range(n):
        a, b = intervals[i]
        beg[i] = a
        end[i] = b + 1

    beg.sort()
    end.sort()

    pa, pb = 0, 0
    cur = 0
    lst = -1

    while pb < n:
        pos = end[pb]
        if pa < n:
            pos = min(pos, beg[pa])

        ans[cur] += pos - lst

        ad = 0
        mn = 0
        while pa < n and beg[pa] == pos:
            ad += 1
            pa += 1
        while pb < n and end[pb] == pos:
            pb += 1
            mn -= 1

        lst = pos
        cur += ad + mn

    for i in range(1, n + 1):
        print(ans[i], end=' ')


if __name__ == "__main__":
    # 示例：运行规模 n=5
    main(5)