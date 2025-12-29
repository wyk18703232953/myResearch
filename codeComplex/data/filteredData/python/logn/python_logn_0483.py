def main(n):
    # 生成与原程序等价的输入：原代码中使用的是 int(input()) - 1
    n = n - 1
    x, y = 1, 9
    # 原始逻辑
    while n > x * y:
        n, x, y = n - x * y, x + 1, 10 * y
    print(str(10 ** (x - 1) + n // x)[n % x])


if __name__ == "__main__":
    # 示例：可以在此处调用 main 进行简单测试
    # 例如 main(1), main(2), main(1000) 等
    main(1000)