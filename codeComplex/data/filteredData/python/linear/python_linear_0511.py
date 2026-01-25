def main(n):
    # n 表示字符串长度
    if n <= 0:
        print(0)
        return

    # 确定性生成 a,b：用 i%2 和 (i//2)%2 构造两种不同的周期模式
    a = [((i % 2) == 1) for i in range(n)]
    b = [(((i // 2) % 2) == 1) for i in range(n)]

    res = 0
    i = 0
    while i + 1 < n:
        if a[i] != b[i] and a[i] != a[i + 1] and b[i] != b[i + 1]:
            a[i] = b[i]
            a[i + 1] = b[i + 1]
            res += 1
            i += 2
        else:
            i += 1

    for i in range(n):
        if a[i] != b[i]:
            res += 1

    print(res)


if __name__ == "__main__":
    # 示例调用，可按需修改 n
    main(10)