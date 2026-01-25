def main(n):
    # 为了进行可规模化的复杂度实验，我们将 n 映射到原程序的三个参数:
    # n_input, d, k（均为确定性函数）
    #
    # 设计目标：
    # - n_input 随 n 线性增长，用于体现规模
    # - d 保持在一个适中范围（避免过小或过大）
    # - k 稍大于 1，避免退化到简单分支
    #
    # 下面是一个简单且确定性的映射方案：
    # n_input = max(2, n)                          保证 n_input >= 2
    # d       = max(1, min(20, n_input // 3))      深度不超过 20
    # k       = 2 + (n_input % 4)                  k ∈ {2,3,4,5}
    n_input = max(2, n)
    d = max(1, min(20, n_input // 3))
    k = 2 + (n_input % 4)

    # 以下是原程序的核心逻辑，保持不变，仅把 input/exit 去掉
    if n_input == 1:
        print("NO")
        return

    if k == 1:
        if n_input == 2 and d == 1:
            print("YES")
            print(1, 2)
        else:
            print("NO")
        return

    if n_input < d + 1:
        print("NO")
        return

    co = 1
    ans = []
    for i in range(1, d + 1):
        ans.append((i, i + 1))
        co += 1

    def dfs(r, dist, co_local):
        if 2 <= r <= d:
            t = k - 2
        else:
            t = k - 1
        if co_local == n_input:
            return co_local
        for _ in range(t):
            if dist == d:
                return co_local
            if co_local == n_input:
                return co_local
            co_local += 1
            ans.append((r, co_local))
            co_local = dfs(co_local, dist + 1, co_local)
        return co_local

    for i in range(2, d + 1):
        co = dfs(i, max(i - 1, d - i + 1), co)

    if co == n_input:
        print("YES")
        for j in ans:
            print(*j)
    else:
        print("NO")


if __name__ == "__main__":
    # 示例：以规模 n=10 运行
    main(10)