def sol(lo, hi, actions, k):
    # 二分搜索满足条件的 eat_candies
    while lo < hi:
        mid = (hi - lo) // 2 + lo
        put_candies = mid * (mid + 1) // 2
        eat_candies = actions - mid
        if put_candies - eat_candies == k:
            return eat_candies
        elif put_candies - eat_candies > k:
            hi = mid - 1
        else:
            lo = mid + 1
    return actions - hi


def main(n):
    # 根据规模 n 生成测试数据：
    # k 在 [0, n*(n+1)//2] 范围内取一个值，这里简单取中间值
    max_diff = n * (n + 1) // 2
    k = max_diff // 2

    res = sol(1, n, n, k)
    print(res)


if __name__ == "__main__":
    # 示例：调用 main(100)
    main(100)