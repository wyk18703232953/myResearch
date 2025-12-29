def main(n: int):
    # 生成测试数据，这里直接使用 n 作为原程序中的 k
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
    # 示例：使用 n = 100 作为规模，可自行修改或在其他模块中调用 main(n)
    main(100)