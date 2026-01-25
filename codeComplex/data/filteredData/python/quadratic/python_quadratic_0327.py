def main(n):
    # 映射：给定规模 n，构造确定性的 (n, d, k)
    # 要求：1 <= d < n，k >= 2，且满足 n >= d+1
    # 下面构造满足这些限制并随 n 变化的确定性参数
    if n < 3:
        # 对于太小的 n，直接不构造树，保持逻辑兼容
        print("NO")
        return

    # 让 d 随 n 增长但小于 n，且至少为 2
    d = max(2, n // 3)
    if d >= n:
        d = n - 1

    # 让 k 随 n 增长，至少 2
    k = max(2, (n // 5) + 2)

    # 以下为原始算法逻辑，仅将输入改为使用上面生成的 n, d, k
    if n < d + 1 or (d > 1 and k == 1):
        print('NO')
        return

    edges = [(1, 2)]
    stack = []
    d2 = d / 2
    d21 = d2 + 1
    for node in range(2, d + 1):
        edges.append((node, node + 1))
        stack.append([node, d2 - abs(d21 - node), k - 2])

    next_i = d + 2
    while next_i <= n:
        if not stack:
            print('NO')
            return

        node = stack[-1]
        i, remaining_depth, remaining_degree = node
        if remaining_depth == 0 or remaining_degree == 0:
            stack.pop()
            continue

        node[2] -= 1
        edges.append((i, next_i))
        stack.append([next_i, remaining_depth - 1, k - 1])
        next_i += 1

    print('YES')
    print('\n'.join(f'{a} {b}' for a, b in edges))


if __name__ == "__main__":
    # 示例：使用 n=20 运行一次以便做时间复杂度实验
    main(20)