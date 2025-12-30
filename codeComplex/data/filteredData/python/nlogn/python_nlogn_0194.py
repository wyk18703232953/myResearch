import random

# 原程序中的最大范围常量
NAX = 200010
BIT_SIZE = NAX * 4 + 5  # 稍微多留一点空间

# Fenwick 树数组
bit = [[0, 0] for _ in range(BIT_SIZE)]

def up(k, val):
    while k < BIT_SIZE:
        bit[k][0] += val
        bit[k][1] += 1
        k += (k & -k)

def go(k):
    ans = 0
    r = 0
    while k > 0:
        ans += bit[k][0]
        r += bit[k][1]
        k -= (k & -k)
    return ans, r

def main(n):
    # 根据 n 生成测试数据，这里生成 n 个 1..n 之间的随机数
    A = [random.randint(1, n) for _ in range(n)]
    N = n

    # 清空 Fenwick 树
    for i in range(BIT_SIZE):
        bit[i][0] = 0
        bit[i][1] = 0

    # 坐标压缩并考虑相邻差 1 的特殊处理
    index = {}
    B = A[:]
    B.sort()
    idx = 1
    index[B[0]] = idx
    for i in range(1, N):
        if B[i] != B[i - 1]:
            if B[i] == B[i - 1] + 1:
                idx += 1
                index[B[i]] = idx
            else:
                idx += 2
                index[B[i]] = idx

    have = 0
    for i in range(N):
        a1, a2 = go(index[A[i]] - 2)
        a3, a4 = go(3 * N)
        a5, a6 = go(index[A[i]] + 1)
        s1 = (a2 * A[i]) - a1
        s2 = ((a4 - a6) * A[i]) - (a3 - a5)
        have += s1
        have += s2
        up(index[A[i]], A[i])

    print(have)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)