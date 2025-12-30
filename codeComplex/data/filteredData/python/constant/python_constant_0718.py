def main(n):
    # 这里将原来的 k 看作规模参数 n
    k = n

    ch = 0
    i = 0
    r = 1
    while k > r - 1:
        r += 9 * (i + 1) * 10 ** i
        i += 1
    r -= 9 * i * 10 ** (i - 1)

    # 按原逻辑计算并输出结果
    print(str((k - r) // i + 10 ** (i - 1))[(k - r) % i])


if __name__ == "__main__":
    # 示例：生成一个测试规模 n 调用 main
    # 可根据需要修改测试数据生成方式
    test_n = 1000
    main(test_n)