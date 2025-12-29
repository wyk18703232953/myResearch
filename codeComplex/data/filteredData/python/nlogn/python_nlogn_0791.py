import random

def main(n):
    # 生成规模为 n 的测试数据
    # 为了保证 N >= K 且有意义，这里选取：
    # N = n，K = max(1, min(n, n // 2))，可按需要调整
    N = n
    if N <= 0:
        return
    K = max(1, min(N, N // 2))  # 1 <= K <= N

    # 生成一个严格递增的数组 A
    # 先生成随机差分，再前缀和
    diffs = [random.randint(1, 10) for _ in range(N)]
    A = []
    cur = 0
    for d in diffs:
        cur += d
        A.append(cur)

    # 原逻辑
    D = sorted([A[i + 1] - A[i] for i in range(N - 1)])
    ans = A[-1] - A[0] - (sum(D[-K + 1:]) if K - 1 else 0)
    print(ans)


if __name__ == "__main__":
    # 示例调用：n 可根据需要修改
    main(10)