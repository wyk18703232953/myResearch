def main(n: int):
    # 根据规模 n 生成测试数据：
    # 这里假设 v 与 n 同阶，例如取 v = n // 2
    v = n // 2

    if n - 1 > v:
        result = v + (n - v + 2) * (n - v - 1) // 2
    else:
        result = n - 1

    print(result)


if __name__ == "__main__":
    # 示例：可在此指定 n 进行测试
    main(10)