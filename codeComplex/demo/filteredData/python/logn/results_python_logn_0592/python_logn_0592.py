def quadratic(a, b, c):
    num = (b * b) - (4 * a * c)
    if num >= 0:
        return [(-b + (num ** 0.5)) / (2.0 * a), (-b - (num ** 0.5)) / (2.0 * a)]

    else:
        return [0.5, 0.5]


def main(n):
    # 根据规模 n 生成测试数据：
    # 这里简单设定 k = n，保持与原问题同数量级
    k = n

    for root in quadratic(1, 3, -2 * n - 2 * k):
        ans = n - root
        if ans > -1:
            # print(int(ans))
            pass
            return


if __name__ == "__main__":
    # 示例调用，可以根据需要修改 n 的值进行测试
    main(10)