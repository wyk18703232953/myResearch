def main(n):
    # n 即原程序中的 k，这里根据规模 n 生成一个测试 k
    # 示例：生成 1 到 n 范围内的一个代表性数值，这里直接取 n
    k = n

    x = 0
    c = 0
    while x < k:
        x += 9 * (10 ** c) * (c + 1)
        c += 1

    p = (x - k) % c
    k_val = (10 ** c) - int((x - k) / c) - 1
    s = str(k_val)
    print(s[len(s) - p - 1])


if __name__ == "__main__":
    # 可以在此处修改 n 作为规模参数进行测试
    main(1000)