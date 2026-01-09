from collections import deque

def solve(n, d, k):
    if n == 1:
        return False, []
    if n == 2:
        if d > 1:
            return False, []

        else:
            return True, [(1, 2)]
    if (not 2 <= d <= n - 1) or k == 1:
        return False, []

    ans = []
    # Build initial chain of length d+1 (d edges)
    for i in range(d):
        ans.append((i + 1, i + 2))
    now = d + 2

    # Expand from internal nodes with BFS under degree constraints
    for i in range(d - 1):
        # depth is the remaining distance budget to keep diameter <= d
        q = deque([(i + 2, min(i, d - i - 2))])
        first = True
        while q and len(ans) < n - 1:
            node, depth = q.popleft()
            end = now + k - 1
            if first:
                # the node already has one edge in the chain
                end -= 1
            for j in range(now, end):
                if len(ans) == n - 1:
                    break
                ans.append((node, j))
                if depth > 0:
                    q.append((j, depth - 1))
            now = end
            first = False

    if len(ans) == n - 1:
        return True, ans

    else:
        return False, []


def main(n):
    """
    根据给定规模 n 生成一组 (d, k) 作为测试数据，
    然后在图构造问题上运行原逻辑。
    返回值为 (ok, edges, d, k)：
      ok: 是否构造成功
      edges: 构造出的边列表
      d, k: 使用的参数
    """
    # 简单的测试数据策略：
    # - n == 1 或 2: 按原逻辑挑一个可行或边界的 d, k
    # - n >= 3: 尝试一个“常规”可行组合 d, k
    if n <= 0:
        raise ValueError("n must be positive")

    if n == 1:
        d, k = 1, 2
    elif n == 2:
        d, k = 1, 2  # 可行：YES, 边为 (1, 2)

    else:
        # 选择一个中等直径和度数，通常可行
        d = min(4, n - 1)
        k = max(2, min(3, n - 1))

    ok, edges = solve(n, d, k)
    return ok, edges, d, k


if __name__ == "__main__":
    # 示例：运行 main(10) 并打印结果，方便直接执行调试
    n = 10
    ok, edges, d, k = main(n)
    if ok:
        # print("YES")
        pass
        # print(f"n={n}, d={d}, k={k}")
        pass
        for u, v in edges:
            # print(u, v)
            pass

    else:
        # print("NO")
        pass
        # print(f"n={n}, d={d}, k={k}")
        pass