def main(n):
    # 依据 n 确定性生成原程序需要的 n, m, a, b
    # 保证 m > 0 且 n, m, a, b 随 n 规模变化
    m = n + 2
    a = (n % 7) + 1
    b = (n % 11) + 2
    original_n = n * 3 + 5

    x = original_n % m
    result = min(a * (m - x), b * x)
    print(result)


if __name__ == "__main__":
    # 示例：用若干不同规模调用 main
    for size in [1, 10, 100, 1000]:
        main(size)