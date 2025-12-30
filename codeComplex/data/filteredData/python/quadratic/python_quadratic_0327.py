import random

def main(n):
    # 生成测试数据：根据规模 n 构造 (n, d, k)
    # 这里选择一个相对宽松的范围，尽量保证有较多 "YES" 的情况
    if n < 2:
        n = 2
    d = random.randint(1, max(1, min(n - 1, 10)))
    k = random.randint(1, max(2, min(n, 10)))

    # 原逻辑开始（移除 input，使用生成的 n, d, k）
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


# 示例调用：按需求只需调用 main(n) 即可
# main(10)