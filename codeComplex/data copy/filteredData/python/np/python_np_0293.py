import math

MOD = 10**9 + 7


def getMul(x):
    a = 1
    for xi in x:
        a *= xi
    return a


def main(n):
    if n <= 0:
        print(0)
        return

    # 确定性生成输入：长度为 n 的整数数组 a
    # 元素分布在 1..n 内，带有重复，以便有意义的因子结构
    a = [i % n + 1 for i in range(n)]

    d = {}
    for ai in a:
        if ai in d:
            d[ai] += 1
        else:
            d[ai] = 1

    max_a = max(a)
    size = max_a + 10

    f = [[] for _ in range(size)]
    for i in range(1, size):
        for j in range(i, size, i):
            f[j].append(i)

    seq = [0 for _ in range(size)]
    for ai in d:
        for fi in f[ai]:
            seq[fi] += d[ai]
    for i in range(size):
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
    for i in range(1, size):
        ans += seq[i] * pf[i]
        ans = (ans + MOD) % MOD
    print(ans)


if __name__ == "__main__":
    main(10)