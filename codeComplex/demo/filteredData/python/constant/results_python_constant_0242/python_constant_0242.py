def power(x, y):
    res = 1
    while y > 0:
        if y % 2 != 0:
            res = res * x
        y //= 2
        x *= x
    return res


def main(n):
    # 根据规模 n 生成测试数据 m，这里简单取 m = n 的平方
    m = n * n

    if n <= 40:
        # print(m % power(2, n))
        pass

    else:
        # print(m)
        pass
if __name__ == "__main__":
    # 示例：调用 main(10)，实际使用时可根据需要修改参数
    main(10)