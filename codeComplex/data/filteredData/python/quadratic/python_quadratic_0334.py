def main(n):
    # 这里根据 n 生成测试数据 (n, d, k)
    # 为了演示，简单设定 d 和 k，可按需要自行调整策略
    # 保证 1 <= d < n，k >= 1
    if n <= 2:
        d = 1
        k = 1

    else:
        d = min(3, n - 1)   # 直径不超过 n-1
        k = min(3, n - 1)   # 每个节点度数上限不超过 n-1

    # 原程序逻辑开始
    if n == 1:
        # print("NO")
        pass
        return

    if k == 1:
        if n == 2 and d == 1:
            # print("YES")
            pass
            # print(1, 2)
            pass

        else:
            # print("NO")
            pass
        return

    if n < d + 1:
        # print("NO")
        pass
        return

    co = 1
    ans = []
    for i in range(1, d + 1):
        ans.append((i, i + 1))
        co += 1

    def dfs(r, dist, co):
        if 2 <= r <= d:
            t = k - 2

        else:
            t = k - 1
        if co == n:
            return co
        for _ in range(t):
            if dist == d:
                return co
            if co == n:
                return co
            co += 1
            ans.append((r, co))
            co = dfs(co, dist + 1, co)
        return co

    for i in range(2, d + 1):
        co = dfs(i, max(i - 1, d - i + 1), co)

    if co == n:
        # print("YES")
        pass
        for j in ans:
            # print(*j)
            pass

    else:
        # print("NO")
        pass
if __name__ == "__main__":
    # 示例：调用 main(10) 进行测试
    main(10)