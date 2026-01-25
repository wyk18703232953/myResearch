def main(n):
    # n 表示后续将要读取的行数（包括第一行）
    # 第一行有 n 个整数；后面 n-1 行也各有 n 个整数
    if n <= 0:
        print(0)
        return

    # 构造第一行数据：1 到 n 的整数
    first_line = list(range(1, n + 1))
    t = sum(first_line)
    r = 1

    # 为了产生有大于 t 的行和小于等于 t 的行，
    # 构造第 i 行为 [i, i+1, ..., i+n-1]
    # 其和为 n*i + n*(n-1)//2
    # 这样行和随 i 单调增加
    for i in range(1, n):
        line_sum = n * i + n * (n - 1) // 2
        if line_sum > t:
            r += 1

    print(r)


if __name__ == "__main__":
    main(5)