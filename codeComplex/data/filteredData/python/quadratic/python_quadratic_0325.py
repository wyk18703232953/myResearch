from collections import deque

def main(n):
    # 映射规则（可调）：给定规模 n，构造 (N, D, K)
    # N 随 n 增长，D 为直径目标，K 为最大度数
    # 保证 1 <= D < N 且 K >= 1
    N = max(2, n)          # 至少 2 个节点
    D = max(1, n // 3)     # 直径目标随 n 缩放
    if D >= N:
        D = N - 1
    K = max(1, (n % 5) + 1)  # 最大度数在 [1, 5] 之间变化

    # 原程序逻辑开始
    if N == 1 or N <= D:
        ans = "NO"
        e = []
    elif K == 1:
        ans = "YES" if N == 2 and D == 1 else "NO"
        e = [(1, 2)] if ans == "YES" else []

    else:
        e = [(i + 1, i + 2) for i in range(D)]
        q = deque()
        l, r = 1, D + 1
        if K > 2:
            for i in range(2, D + 1):
                q.append((i, 2, min(i - l, r - i)))
        ans = "YES"
        for i in range(D + 2, N + 1):
            if not q:
                ans = "NO"
                break
            j, k0, d0 = q.popleft()
            e.append((j, i))
            if k0 + 1 < K:
                q.append((j, k0 + 1, d0))
            if d0 - 1 > 0:
                q.append((i, 1, d0 - 1))

    # 输出用于时间复杂度实验
    # print(ans)
    pass

    if ans == "YES":
        for u, v in e:
            # print(u, v)
            pass
if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 的大小做规模实验
    main(10)