def main(n):
    # 根据规模 n 生成测试数据 m，这里示例取 m = 3 * n
    m = 3 * n

    value = False
    for j in range(n + 1):
        if pow(2, j) > m:
            value = True
            break

    if value:
        print(m)
    else:
        print(m % pow(2, n))


if __name__ == "__main__":
    # 可以在此处指定想要测试的 n
    main(5)