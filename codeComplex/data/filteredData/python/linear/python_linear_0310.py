from collections import defaultdict
import bisect
import random

def main(n):
    # 生成测试数据：
    # 1. 随机选择模数 m（1 <= m <= n，且尽量不太小）
    # 2. 生成长度为 n 的随机数组 a，其中元素为非负整数
    if n <= 0:
        return

    # 这里选择 m 为 [1, n] 中的一个值，可根据需要调整策略
    m = max(1, n // 3)  # 示例：m 约为 n/3
    a = [random.randint(0, 10**9) for _ in range(n)]

    # 以下为原逻辑的无 input() 改写
    rem = [[] for _ in range(m)]
    req = n // m
    ans = 0
    for i in range(n):
        rem[a[i] % m].append([a[i], i])
    ind = m - 1
    for i in range(m):
        size = len(rem[i])
        if size > req:
            ind = i
        if size < req:
            ok = False
            for j in range(ind, ind - m, -1):
                while len(rem[j]) > req:
                    pop, _idx = rem[j].pop()
                    rem[i].append([pop + (i - j) % m, _idx])
                    if len(rem[i]) == req:
                        ok = True
                        break
                if ok:
                    break
                ind -= 1

    out = [0] * n
    for bucket in rem:
        for val, idx in bucket:
            out[idx] = val

    # 输出与原程序一致：第一行为增量和，第二行为数组
    print(sum(out) - sum(a))
    print(' '.join(map(str, out)))


if __name__ == "__main__":
    # 示例：调用 main(10)，可自行修改 n 以测试不同规模
    main(10)