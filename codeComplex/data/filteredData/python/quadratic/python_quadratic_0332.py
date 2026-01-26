def main(n):
    # 输入规模 n 将作为原程序中的 n
    # 为了使实验可规模化且确定，我们用固定的确定性规则生成 d 和 k
    # 约束：d >= 1, k >= 1
    if n < 2:
        n_internal = 2

    else:
        n_internal = n

    # 生成 d：让 d 随 n 增长但不超过 n-1，且至少为 1
    # 使用简单算术构造，保证确定性
    d = max(1, min(n_internal - 1, n_internal // 2))

    # 生成 k：随 n 变化的分支因子，至少为 1
    # 例如：k = (n % 5) + 1，保持在 [1, 6] 之间
    k = (n_internal % 5) + 1

    # 以下为原算法逻辑，仅将 input 改为使用 n_internal, d, k
    n_val, d_val, k_val = n_internal, d, k

    r, odd = divmod(d_val, 2)
    k_val -= 1
    cap = d_val + 1 if k_val == 1 else 1
    if k_val > 1:
        cap = 2 * (k_val ** (r + 1) - 1) // (k_val - 1) if odd else 1 + (k_val + 1) * (k_val ** r - 1) // (k_val - 1)
    if n_val == 1 or k_val < 1 < n_val - 1 or k_val == 1 and d_val != n_val - 1 or d_val >= n_val or k_val > 1 and not d_val < n_val <= cap:
        # print('NO')
        pass
        return

    def dfs(parent, depth, rest, res, k_val_local):
        stack = []
        for _ in range(k_val_local - 1):
            child = rest.pop()
            res.append('%s %s' % (parent, child))
            if depth:
                stack.append((child, depth))
        while stack:
            parent, depth = stack.pop()
            depth -= 1
            for _ in range(k_val_local):
                child = rest.pop()
                res.append('%s %s' % (parent, child))
                if depth:
                    stack.append((child, depth))

    res = ['YES']
    for pc in enumerate(range(2, d_val + 2), 1):
        res.append('%d %d' % pc)
    rest = list(range(n_val, d_val + 1, -1))
    try:
        for p in range(r + 1, r + odd + 2):
            dfs(p, r - 1, rest, res, k_val)
        for de, p, q in zip(range(r - 2, -1, -1), range(r, 1, -1), range(r + odd + 2, d_val + 1)):
            dfs(p, de, rest, res, k_val)
            dfs(q, de, rest, res, k_val)
    except IndexError:
        pass
    # print('\n'.join(res))
    pass
if __name__ == "__main__":
    # 示例调用：可调整不同 n 测试时间复杂度
    main(10)