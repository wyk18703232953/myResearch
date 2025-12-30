import random

def next_pos(A, n, x):
    l = 0
    r = n - 1
    p = -1
    while l <= r:
        m = (l + r) // 2
        if A[m] <= x:
            l = m + 1
        else:
            p = m
            r = m - 1
    return p

def main(n):
    # 规模解释：
    # N = n          士兵堆数
    # Q = n          攻击次数
    N = n
    Q = n

    # 生成测试数据：士兵数量 A 和 每次射箭数量 B
    # A[i] 为每堆士兵数量，正整数
    # B[q] 为第 q 次的箭数，正整数
    random.seed(0)  # 保证复现
    A = [random.randint(1, 10) for _ in range(N)]
    B = [random.randint(1, 10) for _ in range(Q)]

    # 前缀和 P
    P = [A[0]]
    for i in range(1, N):
        P.append(P[i - 1] + A[i])

    soldiers = P[-1]
    arrows = 0

    for q in range(Q):
        arrows += B[q]
        if arrows >= soldiers:
            arrows = 0
            print(N)
        else:
            ind = next_pos(P, N, arrows)
            print(N - ind)

if __name__ == "__main__":
    # 示例：运行规模 n=5
    main(5)