def sum_from_two(x):
    """
    Sum from 2 to x.
    """
    return x * (x + 1) // 2 - 1


def sum_last(k, x):
    """
    Sum which the last `x` splitters can add.
    """
    if x == 0:
        return 1
    # 2 3 4 ... k. <- We have these splitters.
    # x == 1, just k. sum(2, k) - sum(2, k - x)
    # Each item k_i gives sum k_i - 1
    # Add 1 for initial pipes.
    return sum_from_two(k) - sum_from_two(k - x) - x + 1


def possible(n, k, x):
    return sum_last(k, x) >= n


def solve(n, k):
    """
    原始逻辑封装：根据 n, k 计算答案。
    """
    if n == 1:
        # Already have 1.
        return 0

    # Can't use any of the splitters.
    if sum_last(k, k - 1) < n:
        return -1

    # Use only one splitter.
    minimum = 1
    # Can use at most k - 1 splitters.
    maximum = k - 1
    while minimum <= maximum:
        if minimum == maximum:
            return minimum
        elif minimum == maximum - 1:
            if possible(n, k, minimum):
                return minimum
            else:
                return maximum

        mid = (minimum + maximum) // 2
        if possible(n, k, mid):
            # Try if smaller is possible.
            maximum = mid
        else:
            # Need more.
            minimum = mid


def main(n):
    """
    n 为规模参数，用于生成测试数据 (n, k)，并返回算法结果。

    测试数据生成策略（可按需要调整）：
    - n_data = n
    - k 取一个与 n 相关的值，这里简单设为 max(2, n)
    """
    n_data = n
    k = max(2, n)   # 生成一个与规模相关的 k
    return solve(n_data, k)


if __name__ == "__main__":
    # 示例：调用 main(10) 做一次测试
    result = main(10)
    print(result)