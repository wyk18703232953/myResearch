def sol(n, k):
    p = 1
    q = 1
    acc = 0
    while n > 0 and k >= p:
        k -= p
        n -= 1
        if n >= 40:
            return n
        acc += q * (4 ** n - 1) // 3
        if k <= acc:
            return n
        p = 2 * p + 1
        q = 2 * q + 3
    return -1


def main(n):
    """
    n: 测试规模，表示生成 n 组 (n_i, k_i) 测试数据并求解。
    这里的 n 既是测试组数，也是每组中 n_i 的上限。
    """
    # 生成测试数据并调用 sol
    for i in range(1, n + 1):
        # 测试数据生成策略：
        # n_i 从 1 到 n，k_i 取一个与 n_i 相关的值，保证多样性
        n_i = i
        # 上界取一个较大的数，以便部分用例触发不同分支
        k_i = i * i + 3 * i + 7

        ans = sol(n_i, k_i)
        if ans == -1:
            # print("NO")
            pass

        else:
            # print("YES", ans)
            pass
if __name__ == "__main__":
    # 示例：调用 main(5) 生成 5 组测试数据并输出结果
    main(5)