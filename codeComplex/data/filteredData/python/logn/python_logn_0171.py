def sum_from_two(x: int) -> int:
    """
    Sum from 2 to x.
    """
    return x * (x + 1) // 2 - 1


def sum_last(k: int, x: int) -> int:
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


def possible(n: int, k: int, x: int) -> bool:
    return sum_last(k, x) >= n


def solve(n: int, k: int) -> int:
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


def main(n: int):
    # 根据规模 n 生成测试数据：
    # 这里设定 k 与 n 相关，例如 k = 2 * n（可根据需求调整）
    if n <= 0:
        return None
    k = 2 * n
    return solve(n, k)


if __name__ == "__main__":
    # 示例：调用 main(10) 进行测试
    result = main(10)
    # print(result)
    pass