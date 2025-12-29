def sum_range(x):
    return (x * (x + 1)) // 2


def bs(st, en, n, k, s):
    while st < en:
        mid = st + (en - st) // 2
        s1 = s - sum_range(mid - 1)

        if s1 == n:
            return (k - mid) + 1
        elif s1 > n:
            st = mid + 1
        else:
            en = mid
    return (k - st) + 2


def main(n):
    # 根据规模 n 生成测试数据
    # 原程序逻辑依赖 n 和 k：
    #   1 <= n <= ...
    #   0 <= k <= n-1 （因为后面有 n-1, k-1）
    # 这里简单设置 k = max(1, n // 2)，并保证 k < n
    if n <= 1:
        # 与原逻辑对应：如果输入的 (n+1) == 1，即 n == 0，则输出 0
        # 此处生成的数据无法满足 n-1 >= 0 时的正常流程，直接返回与原逻辑一致的输出
        print(0)
        return

    k = max(1, n // 2)
    if k >= n:
        k = n - 1

    # 对应原始代码中的预处理
    n_adj = n - 1
    k_adj = k - 1
    s = sum_range(k_adj)

    if n_adj + 1 == 1:
        print(0)
    elif n_adj <= k_adj:
        print(1)
    elif n_adj > s:
        print(-1)
    else:
        print(bs(1, k_adj, n_adj, k_adj, s))


if __name__ == "__main__":
    # 示例：调用 main，规模 n 可根据需要调整
    main(10)