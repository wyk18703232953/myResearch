import random

def main(n: int):
    # 生成测试数据
    N = n  # 数组规模
    Q = n  # 查询次数，也设为 n，可按需要调整策略

    # 生成一个包含 0~10^9 之间随机整数的数组
    A = [random.randint(0, 10**9) for _ in range(N)]

    # 随机生成 Q 个区间 [l, r]，1-based
    queries = []
    for _ in range(Q):
        l = random.randint(1, N)
        r = random.randint(l, N)
        queries.append((l, r))

    # 以下是原始逻辑

    cnt = 0
    for i in range(N):
        for j in range(i + 1, N):
            if A[i] > A[j]:
                cnt += 1

    cnt %= 2

    Ans = [None] * Q
    for qu in range(Q):
        l, r = queries[qu]
        if (r - l + 1) * (r - l) // 2 & 1:
            cnt ^= 1

        Ans[qu] = 'odd' if cnt else 'even'

    print('\n'.join(Ans))


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)