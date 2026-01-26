def f(i):
    return (10 ** i - 10 ** (i - 1)) * i

def main(n):
    i = 1
    total = 0
    m = n  # 使用可变副本进行计算
    while m - f(i) >= 0:
        m -= f(i)
        total += f(i) // i
        i += 1

    # 原程序输出的是一个数字字符，这里保持行为一致，返回字符
    return str(total + (m + i - 1) // i)[m % i - 1]


if __name__ == "__main__":
    # 简单的测试数据生成：按题意，直接使用给定 n 调用 main
    # 可以根据需要在这里替换或增加不同规模的 n 进行测试
    test_n = 100  # 示例规模，可修改
    result = main(test_n)
    # print(result)
    pass