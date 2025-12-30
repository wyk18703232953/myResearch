def main(n: int):
    # 根据规模 n 生成测试数据，这里假定测试数据本身就是整数 n
    x = 1
    n -= 1
    y = 9
    while n > x * y:
        n -= x * y
        y *= 10
        x += 1
    a = (8 + 2) ** (x - 1)
    a += n // x
    print(str(a)[n % x])


if __name__ == "__main__":
    # 示例：使用 n = 100 作为测试规模
    main(100)