def main(n):
    # 由 n 生成测试数据，这里直接使用 n 作为输入规模
    k = n - 1
    x, y = 1, 9
    while k > x * y:
        k, x, y = k - x * y, x + 1, y * 10
    result_digit = str(10 ** (x - 1) + k // x)[k % x]
    # print(result_digit)
    pass
if __name__ == "__main__":
    # 示例：调用 main(15)，可根据需要修改 n 的值做测试
    main(15)