def main(n: int):
    # 这里将 n 直接作为规模和逻辑中的 n（即“第 n 位”）
    x, y = 1, 9
    n -= 1
    while n > x * y:
        n -= x * y
        x += 1
        y *= 10
    a = 10 ** (x - 1) + n // x
    # print(str(a)[n % x])
    pass
if __name__ == "__main__":
    # 示例：根据规模 n 生成测试数据
    # 你可以在这里修改要测试的 n 值
    test_n = 1000
    main(test_n)