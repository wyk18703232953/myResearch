def main(n):
    # 映射含义：
    # N = n，K = n//2 + 1，A 为长度为 N 的确定性整数序列
    N = max(2, n)
    K = min(N, max(1, N // 2 + 1))

    # 确定性生成 A：严格递增，差值有变化便于保持原逻辑
    A = [i * (i % 5 + 1) for i in range(N)]

    D = sorted([A[i + 1] - A[i] for i in range(N - 1)])
    result = A[-1] - A[0] - (sum(D[-K + 1:]) if K - 1 else 0)
    print(result)


if __name__ == "__main__":
    main(10)