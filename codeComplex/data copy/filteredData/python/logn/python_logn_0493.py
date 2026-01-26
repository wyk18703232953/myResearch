def main(n):
    # n 即原程序中的 k，这里根据规模 n 直接设定为 n
    k = n

    i = 0
    r = 1
    while k >= r:
        r += 9 * (i + 1) * 10 ** i
        i += 1
    r = r - (9 * i * 10 ** (i - 1))
    ans = str(((k - r) // i) + 10 ** (i - 1))[(k - r) % i]
    # print(ans)
    pass
if __name__ == "__main__":
    # 示例：根据规模生成测试数据，这里直接用 n 本身作为 k
    # 可按需修改为其它生成方式
    test_n = 1000
    main(test_n)