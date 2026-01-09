def maximum_candies_after_n_movies(n):
    return n * (n + 1) // 2


def solve(n, k):
    upper_bound = n
    lower_bound = 0
    while upper_bound > lower_bound:
        if upper_bound == lower_bound + 1:
            u_c = maximum_candies_after_n_movies(upper_bound)
            if u_c == k:
                return n - upper_bound

        middle = (upper_bound + lower_bound) // 2
        m_candies = maximum_candies_after_n_movies(middle) - (n - middle)
        if m_candies == k:
            return n - middle
        elif m_candies < k:
            lower_bound = middle

        else:
            upper_bound = middle
    return None


def main(n):
    # 根据规模 n 生成测试数据
    # 这里选择一种简单生成方式：随机一个吃掉的数量 e (0 <= e <= n)，
    # 计算对应的 k，然后再利用 solve(n, k) 求回 e。
    # 为保证确定性，这里不使用随机，而是固定取 e = n // 2。
    eaten = n // 2
    k = maximum_candies_after_n_movies(n - eaten)

    result = solve(n, k)
    if result is not None:
        # print(result)
        pass

    else:
        # print("No valid solution found")
        pass
if __name__ == "__main__":
    # 示例：调用 main，规模可自行修改
    main(10)