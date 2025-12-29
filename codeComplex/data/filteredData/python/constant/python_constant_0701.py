def main(n: int):
    # 根据规模 n 生成测试数据，这里演示设定 v 为中间位置
    v = max(1, min(n, n // 2 + 1))

    if n - 1 > v:
        result = v - 1 + (n - v) * (n - v + 1) // 2
    else:
        result = n - 1

    print(result)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)