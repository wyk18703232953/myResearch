import sys
import random

MOD = 10**9 + 7
sys.setrecursionlimit(1_000_000)


def getMul(x):
    a = 1
    for xi in x:
        a *= xi
    return a


def main(n):
    # 1. 根据规模 n 生成测试数据 a
    #    这里生成 n 个随机整数，范围 [1, 10^6]
    max_val = 10**6
    a = [random.randint(1, max_val) for _ in range(n)]

    # 2. 原始逻辑开始
    d = {}
    for ai in a:
        if ai in d:
            d[ai] += 1
        else:
            d[ai] = 1

    max_a = max(a) if a else 0
    size = max_a + 10

    f = [[] for _ in range(size)]
    for i in range(1, size):
        for j in range(i, size, i):
            f[j].append(i)

    seq = [0 for _ in range(size)]
    for ai in d:
        for fi in f[ai]:
            seq[fi] += d[ai]
    for i in range(len(seq)):
        seq[i] = (pow(2, seq[i], MOD) - 1 + MOD) % MOD

    pf = [[] for _ in range(size)]
    pf[0] = None
    pf[1].append(1)
    for i in range(2, size):
        if len(pf[i]) == 0:
            for j in range(i, size, i):
                pf[j].append(i)
    for i in range(1, size):
        mul = getMul(pf[i])
        if mul == i:
            if len(pf[i]) & 1 == 1:
                pf[i] = -1
            else:
                pf[i] = 1
        else:
            pf[i] = 0
    pf[1] = 1

    ans = 0
    for i in range(1, len(seq)):
        ans += seq[i] * pf[i]
        ans = (ans + MOD) % MOD

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main，规模 n 可自行修改
    main(10)