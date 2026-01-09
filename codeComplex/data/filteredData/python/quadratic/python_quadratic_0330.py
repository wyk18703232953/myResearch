def main(n):
    # 根据规模 n 自动生成一组 (n, d, k) 测试参数
    # 这里给出一个简单策略，确保大多数情况下可以构造出解：
    # - d: 直径，介于 1 和 n-1 之间
    # - k: 每个结点最大度数，至少为 2
    if n <= 1:
        d = 0
        k = 0
    elif n == 2:
        d = 1
        k = 1

    else:
        # 尝试选择一个适中的直径与较大的度数，增加构造成功概率
        d = max(1, min(n - 1, n // 3))
        if d == 1:
            k = max(2, n - 1)  # 星形树

        else:
            k = 3

    num = d + 2  # 与原程序保持一致
    # 将 n, d, k 封装到 solve 内部，避免使用全局变量
    def solve(n, d, k):
        nonlocal num
        if n == 1:
            return 'NO'
        if n == 2:
            if d != 1:
                return 'NO'

            else:
                return "YES\n1 2"
        if k < 2:
            return 'NO'
        if d > n - 1:
            return 'NO'

        depth = [min(i, d - i) for i in range(d + 1)]
        ans = [(i + 1, i + 2) for i in range(d)]

        def dfs(v, dep):
            nonlocal num
            if dep == 0:
                return
            for _ in range(k - 1):
                if len(ans) == n - 1:
                    return
                v2 = num
                num += 1
                ans.append((v, v2))
                dfs(v2, dep - 1)

        for v in range(d + 1):
            if depth[v] == 0:
                continue
            for _ in range(k - 2):
                if len(ans) == n - 1:
                    break
                v2 = num
                num += 1
                ans.append((v + 1, v2))
                if depth[v] > 1:
                    dfs(v2, depth[v] - 1)

        if len(ans) < n - 1:
            return "NO"
        return "YES\n%s" % "\n".join("%d %d" % e for e in ans)

    return solve(n, d, k)


# 例如：直接运行文件时，用一个默认 n 进行演示
if __name__ == "__main__":
    n_demo = 10
    # print(main(n_demo))
    pass