def main(n):
    # 根据规模 n 生成测试数据，这里示例令 k = n
    k = n

    c = n + k
    p = int(0.5 * ((8 * c + 9) ** 0.5 - 3))
    result = n - p

    print(result)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)