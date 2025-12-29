def main(n):
    # 这里的 n 视为“规模参数”，我们按题目原逻辑生成一个测试用 n_val
    # 原问题逻辑是对 1 开始的正整数序列的“数字序号”访问，因此生成一个较大的 n_val 以测试逻辑
    # 例如：令 n_val = n^2，当然可按需要调整生成规则
    n_val = n * n - 1  # 对应原代码中的 int(input()) - 1

    x, y = 1, 9
    while n_val > x * y:
        n_val, x, y = n_val - x * y, x + 1, y * 10
    a = str(10 ** (x - 1) + n_val // x)[n_val % x]
    print(a)


if __name__ == "__main__":
    # 举例：调用 main(10)
    main(10)