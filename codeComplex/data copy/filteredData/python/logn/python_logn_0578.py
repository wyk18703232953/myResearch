def main(n: int):
    # 这里假设规模 n 直接对应原程序中的 n（即原来输入的是 n+1）
    n = n - 1
    x, y = 1, 9
    while n > x * y:
        n, x, y = n - x * y, x + 1, y * 10
    a = str(10 ** (x - 1) + n // x)[n % x]
    # print(a)
    pass
if __name__ == "__main__":
    # 根据规模 n 生成测试数据并调用 main(n)
    # 示例：可根据需要修改测试的 n 值
    test_n = 1000  # 例如：第 1000 位
    main(test_n)