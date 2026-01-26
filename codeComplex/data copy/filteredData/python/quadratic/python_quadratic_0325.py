def main(n):
    # 为了进行可规模化的复杂度实验，将原本的 3 个输入参数 (n, d, k)
    # 全部由单一规模参数 n 决定，采用确定性的映射：
    #   N = max(1, n)                -> 原代码中的 n（节点数）
    #   d = max(1, min(N - 1, n // 3 + 1))
    #   k = max(1, min(N, n // 5 + 2))
    #
    # 这样随着 n 增大，节点数 N、参数 d、k 都会随之增长，并且是完全确定性的。
    N = max(1, n)
    d = max(1, min(N - 1 if N > 1 else 1, n // 3 + 1))
    k = max(1, min(N, n // 5 + 2))

    if N == 1 or N <= d:
        ans = "NO"
        e = []
    elif k == 1:
        ans = "YES" if N == 2 and d == 1 else "NO"
        e = [(1, 2)]

    else:
        e = [(i + 1, i + 2) for i in range(d)]
        from collections import deque
        q = deque()
        l, r = 1, d + 1
        if k > 2:
            for i in range(2, d + 1):
                q.append((i, 2, min(i - l, r - i)))
        ans = "YES"
        for i in range(d + 2, N + 1):
            if not q:
                ans = "NO"
                break
            j, k0, d0 = q.popleft()
            e.append((j, i))
            if k0 + 1 < k:
                q.append((j, k0 + 1, d0))
            if d0 - 1 > 0:
                q.append((i, 1, d0 - 1))

    # print(ans)
    pass

    if ans == "YES":
        for u, v in e:
            # print(u, v)
            pass
if __name__ == "__main__":
    # 示例：使用 n = 100 进行一次规模为 100 的测试
    main(100)