def main(n):
    # 根据规模 n 生成测试数据
    # 这里假设 v 在 [0, n] 范围内，示例用 n 的一半作为测试值
    v = n // 2

    if v >= (n - 1):
        result = n - 1
    else:
        result = int((((n - v) * (n - v + 1)) / 2) - 1 + v)

    print(result)


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    main(10)