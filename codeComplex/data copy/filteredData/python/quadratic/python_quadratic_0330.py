def main(n):
    # 映射输入规模 n -> (n_nodes, d, k)
    # 确保 n >= 2
    if n < 2:
        n = 2
    n_nodes = n
    d = max(1, n_nodes // 3)
    k = 3

    num = d + 2

    def solve():
        nonlocal num, n_nodes, d, k
        if n_nodes == 1:
            return 'NO'
        if n_nodes == 2:
            if d != 1:
                return 'NO'

            else:
                return "YES\n1 2"
        if k < 2:
            return 'NO'
        if d > n_nodes - 1:
            return 'NO'

        depth = [min(i, d - i) for i in range(d + 1)]
        ans = [(i + 1, i + 2) for i in range(d)]

        def dfs(v, depth_left):
            nonlocal num, ans, n_nodes, k
            if depth_left == 0:
                return
            for _ in range(k - 1):
                if len(ans) == n_nodes - 1:
                    return
                v2 = num
                num += 1
                ans.append((v, v2))
                dfs(v2, depth_left - 1)

        for v in range(d + 1):
            if depth[v] == 0:
                continue
            for _ in range(k - 2):
                if len(ans) == n_nodes - 1:
                    break
                v2 = num
                num += 1
                ans.append((v + 1, v2))
                if depth[v] > 1:
                    dfs(v2, depth[v] - 1)

        if len(ans) < n_nodes - 1:
            return "NO"
        return "YES\n%s" % "\n".join(["%d %d" % i for i in ans])

    result = solve()
    # print(result)
    pass
if __name__ == "__main__":
    main(10)