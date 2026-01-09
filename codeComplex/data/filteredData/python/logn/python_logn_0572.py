def main(n):
    # 这里将 n 作为原程序中的 k 使用
    k = n

    mul = 1
    d = 1

    while k > mul * 9 * d:
        k -= mul * 9 * d
        d += 1
        mul *= 10

    x = k % d
    y = k // d
    y += mul

    if x == 0:
        ans = (y - 1) % 10

    else:
        y = y // pow(10, d - x)
        ans = y % 10

    # print(ans)
    pass
if __name__ == "__main__":
    # 示例：可在此处指定规模 n 进行测试
    # 例如 n = 1000
    main(1000)