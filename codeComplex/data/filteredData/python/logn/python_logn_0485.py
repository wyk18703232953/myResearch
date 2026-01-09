def dfs2(root, par):
    global dp, kthpar, gp
    if par != -1:
        dp[root] = dp[par] + 1
    for i in range(1, 20):
        if kthpar[root][i - 1] != -1:
            kthpar[root][i] = kthpar[kthpar[root][i - 1]][i - 1]
    for child in gp[root]:
        if child == par:
            continue
        kthpar[child][0] = root
        dfs(child)


def dfs(root):
    global tot, vis, gp
    for child in gp[root]:
        if vis[child] == 0:
            tot += 1
            vis[child] = 1
            dfs(child)


def hnbhai_single_query(n):
    d, num = 0, 1
    while num <= n:
        num += 9 * (d + 1) * (10 ** d)
        d += 1
    num -= 9 * (d) * (10 ** (d - 1))
    ans = str(10 ** (d - 1) + (n - num) // d)
    return ans[(n - num) % d]


def main(n):
    global gp, dp, kthpar, vis, tot
    # Prepare some deterministic graph-related globals to keep structure similar
    # Build a simple path graph of size n for potential dfs usage
    size = max(1, n)
    gp = [[] for _ in range(size)]
    for i in range(size - 1):
        gp[i].append(i + 1)
        gp[i + 1].append(i)

    dp = [0] * size
    kthpar = [[-1] * 20 for _ in range(size)]
    vis = [0] * size
    tot = 0

    if size > 0:
        vis[0] = 1
        dfs(0)
        kthpar[0][0] = -1
        dfs2(0, -1)

    # Use the core logic: treat n as the single query value
    # Ensure n is positive for the original logic; if n <= 0, define a simple behavior
    query = max(1, n)
    result_char = hnbhai_single_query(query)
    # print(result_char)
    pass
if __name__ == "__main__":
    main(10)