def sum_1(n):
    s = n * (n + 1) // 2
    return s

def sum_2(s, e):
    if s <= 1:
        return sum_1(e)
    return sum_1(e) - sum_1(s - 1)

def mini_splitter(k, n):
    st = 1
    end = k
    while st < end:
        mid = (st + end) // 2
        s = sum_2(mid, k)
        if s == n:
            return k - mid + 1
        elif s > n:
            st = mid + 1
        else:
            end = mid
    return k - st + 2

def solve_case(n, k):
    if n == 1:
        return 0
    elif n <= k:
        return 1
    else:
        k -= 1
        n -= 1
        if sum_1(k) < n:
            return -1
        else:
            return mini_splitter(k, n)

def main(n):
    """
    n: 规模参数，用于生成测试数据。
    这里假定原问题需要两个参数 (n, k)：
    - n_data 为原代码中的 n
    - k_data 为原代码中的 k
    根据规模 n 生成一组合理的 (n_data, k_data) 作为测试数据。
    """
    # 简单的测试数据生成策略：
    # 保证 k_data 至少为 1，且适度大于等于 n_data，覆盖不同情况。
    n_data = max(1, n)
    # 令 k_data 在 [1, 2*n_data] 范围内（含边界）
    k_data = max(1, 2 * n_data)

    ans = solve_case(n_data, k_data)
    print(ans)

if __name__ == "__main__":
    # 示例：用某个规模参数运行
    main(10)