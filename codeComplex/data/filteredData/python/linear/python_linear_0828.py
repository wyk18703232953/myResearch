import random

def main(n):
    """
    n: 规模，用来生成测试数据的 N 和 Q
    这里简单设定：
      Q = max(1, n // 5)
      每个测试的 N = n
      K 在 [1, N] 中随机
      S 为长度 N 的随机 'R','G','B' 字符串
    """
    Q = max(1, n // 5)
    results = []

    for _ in range(Q):
        N = n
        K = random.randint(1, N)
        S = ''.join(random.choice('RGB') for _ in range(N))

        X = [{"R": 0, "G": 1, "B": 2}[s] for s in S]
        mi = K
        for i in range(3):
            d = 0
            for j in range(N):
                if X[j] != (i + j) % 3:
                    d += 1
                if j >= K and X[j - K] != (i + j - K) % 3:
                    d -= 1
                if j >= K - 1:
                    mi = min(mi, d)
        results.append(mi)

    # 输出结果
    for ans in results:
        print(ans)


if __name__ == "__main__":
    # 示例：规模为 20
    main(20)