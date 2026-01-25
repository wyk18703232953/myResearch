def main(n):
    # n 表示数组长度
    if n <= 0:
        print(0)
        return

    # 确定性生成测试数据：a[i] = (i + 1) * (i % 5 + 1)
    a = [(i + 1) * (i % 5 + 1) for i in range(n)]

    a.sort()
    ans = 0
    while a:
        m = a[0]
        b = []
        for x in a[1:]:
            if x % m != 0:
                b.append(x)
        a = b
        ans += 1
    print(ans)


if __name__ == "__main__":
    main(10)