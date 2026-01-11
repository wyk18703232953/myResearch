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
    # 定义输入规模映射：
    # N = n（士兵数量）
    # Q = n（询问数量）
    N = n
    Q = n

    # 确定性构造 A 和 B
    # A: 每个士兵的生命值，使用周期性模式 (i % 5) + 1，保证为正
    A = [(i % 5) + 1 for i in range(N)]
    # B: 每次攻击的箭数，使用 (i % 7) + 1
    B = [(i % 7) + 1 for i in range(Q)]

    P = [A[0]]
    for i in range(1, N):
        P.append(P[i - 1] + A[i])

    soldiers = P[-1]
    arrows = 0

    for q in range(Q):
        arrows += B[q]
        if arrows >= soldiers:
            arrows = 0
            # print(N)
            pass

        else:
            ind = next_pos(P, N, arrows)
            # print(N - ind)
            pass
if __name__ == "__main__":
    main(10)