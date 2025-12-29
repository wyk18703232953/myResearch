def main(n: int):
    # 生成规模为 n 的测试数据（此处直接使用 n 作为原始代码中的 n）
    if n == 1:
        print(1)
        return

    y = n
    i = 1
    while n != 0:
        j = n // 2 + n % 2
        if i * 2 > y and n == 1:
            i = i >> 1
            x = y // i
            print(i * x)
        else:
            print((str(i) + ' ') * j, end='')
        i = i << 1
        n = n // 2


if __name__ == "__main__":
    # 示例：可以在这里修改 n 测试不同规模
    main(10)