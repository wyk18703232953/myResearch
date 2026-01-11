from sys import stdout

memo = {}


def max_splits(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n in memo:
        return memo[n]
    result = 4 * max_splits(n - 1) + 1
    memo[n] = result
    return result


def solve_single_case(n, k):
    min_splits = 1
    path_count = 3

    if n > 75:
        return "YES", n - 1

    square_size = n - 1
    max_buffer = max_splits(square_size)

    while min_splits + path_count <= k and square_size > 0:
        min_splits += path_count
        max_buffer += (4 * path_count - (2 * path_count + 1)) * max_splits(square_size - 1)
        path_count = 2 * path_count + 1
        square_size -= 1

    if min_splits <= k <= min_splits + max_buffer:
        return "YES", square_size

    else:
        return "NO", None


def generate_test_data(n):
    """
    生成规模为 n 的测试数据：
    - t = n 个测试用例
    - 对于第 i 个测试:
        n_i 在 [1, max(1, n)] 范围内
        k_i 在 [1, 10^6] 范围内，简单按公式生成
    """
    t = n
    cases = []
    max_n = max(1, n)
    for i in range(1, t + 1):
        ni = (i % max_n) + 1  # 1..max_n 循环
        ki = (i * i * 1234567) % 1_000_000 + 1
        cases.append((ni, ki))
    return t, cases


def main(n):
    """
    n 为规模参数，用来生成 n 个测试用例并运行原逻辑。
    输出格式与原程序一致：每个用例一行，输出 YES x 或 NO。
    """
    global memo
    memo = {}

    t, cases = generate_test_data(n)
    out_lines = []

    for ni, ki in cases:
        res, val = solve_single_case(ni, ki)
        if res == "YES":
            out_lines.append(f"YES {val}")

        else:
            out_lines.append("NO")

    # stdout.write("\n".join(out_lines))


if __name__ == "__main__":
    # 示例：以 n = 5 运行一遍
    main(5)