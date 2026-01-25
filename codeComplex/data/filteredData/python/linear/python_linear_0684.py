def main(n):
    # n 作为 b 的长度，生成一个确定性的 b 序列
    if n <= 0:
        return
    # 使用简单的算术构造 b
    b = [(i * 3 + 1) % (n * 5 + 7) + 1 for i in range(n)]
    a = [0] * (2 * len(b))
    a[-1] = b[0]
    for i in range(1, len(b)):
        if b[i] - a[i - 1] <= a[-i]:
            a[i] = a[i - 1]
            a[-i - 1] = b[i] - a[i - 1]
        else:
            a[-i - 1] = a[-i]
            a[i] = b[i] - a[-i - 1]
    print(*a)


if __name__ == "__main__":
    main(10)