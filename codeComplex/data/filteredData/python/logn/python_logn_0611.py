def maximum_candies_after_n_movies(n):
    return n * (n + 1) // 2


def solve1(n, k):
    m = maximum_candies_after_n_movies(n)
    current_candies = n
    eaten_candies = 0
    while m != k:
        m = m - current_candies - 1
        current_candies -= 1
        eaten_candies += 1
    return eaten_candies


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
    # 定义输入规模: n 为原题中的 n，上界不小于 1
    if n < 1:
        n = 1

    # 确定性生成 k：
    # 原逻辑中，k 是吃掉若干颗糖后的剩余糖数；
    # 这里用“吃掉 n//2 次”的结果作为 k，保证一定有解。
    eat_times = n // 2
    total = maximum_candies_after_n_movies(n)
    k = total
    current_candies = n
    for _ in range(eat_times):
        k = k - current_candies - 1
        current_candies -= 1

    ans = solve(n, k)
    print(ans)


if __name__ == "__main__":
    # 示例调用，可按需要修改 n 的规模
    main(10)