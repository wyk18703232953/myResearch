import random

def main(n):
    # 生成测试数据
    # Q：查询个数，设为 n
    Q = n
    # 为每个查询生成 (N, K, S)
    # N 在 [1, n] 内，K 在 [1, N] 内，S 为长度为 N 的随机 RGB 串
    D = {"R": 0, "G": 1, "B": 2}
    colors = ["R", "G", "B"]

    queries = []
    for _ in range(Q):
        N = random.randint(1, n)
        K = random.randint(1, N)
        S = "".join(random.choice(colors) for _ in range(N))
        queries.append((N, K, S))

    # 原逻辑
    results = []
    for (N, K, S) in queries:
        mi = K
        for i in range(3):
            d = 0
            for j in range(N):
                if D[S[j]] != (i + j) % 3:
                    d += 1
                if j >= K and D[S[j - K]] != (i + j - K) % 3:
                    d -= 1
                if j >= K - 1:
                    mi = min(mi, d)
        results.append(mi)

    # 输出结果
    for ans in results:
        print(ans)


if __name__ == "__main__":
    # 可以在此处调整 n 的大小做简单测试
    main(10)