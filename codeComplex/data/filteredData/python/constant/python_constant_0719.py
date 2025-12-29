def main(n):
    # 这里将原来的 k 替换为 n 作为规模参数
    k = n

    i = 0
    r = 1
    while k >= r:
        r += 9 * (i + 1) * 10 ** i
        i += 1
    r = r - (9 * i * 10 ** (i - 1))
    ans = str(((k - r) // i) + 10 ** (i - 1))[(k - r) % i]
    print(ans)


if __name__ == "__main__":
    # 示例：使用 n = 100 作为测试规模
    main(100)