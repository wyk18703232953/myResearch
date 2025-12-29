def good(max_branch, s, n):
    nodes = 0
    can = 1
    lowest_s = 0
    depth = 1
    while nodes < n:
        added = min(n - nodes, can)
        lowest_s += added * depth
        nodes += added
        can *= max_branch
        depth += 1
    return lowest_s <= s


def solve_one(n, s):
    if s < 2 * n - 1 or s * 2 > n * (n + 1):
        return "No", []

    lo, hi = 1, n
    while lo < hi:
        mid = (lo + hi) >> 1
        if not good(mid, s, n):
            lo = mid + 1
        else:
            hi = mid

    max_branch = lo

    level_size = [1] * (n + 1)
    node_level = [i for i in range(n + 1)]
    cur_node = n
    cur_level = 1
    cur_sum = n * (n + 1) // 2
    can = 1
    while cur_sum > s:
        if level_size[cur_level] == can:
            cur_level += 1
            can *= max_branch

        if cur_sum - (cur_node - cur_level) < s:
            cur_level = cur_node - (cur_sum - s)

        node_level[cur_node] = cur_level
        level_size[cur_level] += 1
        cur_sum -= cur_node - cur_level
        cur_node -= 1

    node_list = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        node_list[node_level[i]].append(i)

    children = [0] * (n + 1)
    parent = [-1] * (n + 1)
    seen_nodes = 1
    for level in range(2, n + 1):
        idx = 0
        if not node_list[level - 1]:
            break
        cur_father = node_list[level - 1][0]
        for node in node_list[level]:
            if children[cur_father] == max_branch:
                idx += 1
                cur_father = node_list[level - 1][idx]
            children[cur_father] += 1
            parent[node] = cur_father
            seen_nodes += 1

    return "Yes", parent[2:]


def main(n):
    """
    生成规模为 n 的一组测试数据，并运行原逻辑。

    这里按照允许的 sum(s) 范围：
        2n-1 <= s <= n(n+1)/2
    自动构造一个中间值 s 作为测试数据。
    """
    if n <= 0:
        return

    min_s = 2 * n - 1
    max_s = n * (n + 1) // 2
    s = (min_s + max_s) // 2  # 取一个中间值作为测试数据

    ans, parents = solve_one(n, s)
    print(ans)
    if ans == "Yes":
        print(*parents)


# 示例：直接运行时可以调用 main，例如：
# if __name__ == "__main__":
#     main(5)