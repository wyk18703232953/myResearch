def main(n: int):
    # 根据 n 生成测试数据：令 m 为 0 到 2^(n+1) 范围内的某个值
    # 这里简单设为 m = 2^n - 1，确保既能覆盖 m < 2^n 的情况
    m = (1 << n) - 1  # 等价于 2**n - 1

    value = False
    for j in range(n + 1):
        if (1 << j) > m:  # 等价于 pow(2, j)
            value = True
            break

    if value:
        print(m)
    else:
        print(m % (1 << n))


if __name__ == "__main__":
    # 示例：调用 main(5)，可按需修改或在外部导入调用 main(n)
    main(5)