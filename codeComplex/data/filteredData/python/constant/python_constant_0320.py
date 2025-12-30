def main(n):
    # 根据 n 生成测试数据，这里示例为前 14 个自然数循环填充
    # 原程序逻辑固定在 14 个坑位上运算，所以只取前 14 个作为 l
    l = [(i % n) + 1 for i in range(14)]

    ans = 0
    for i in range(14):
        a = []
        m = 0
        a.extend(l)
        c = a[i] // 14
        d = a[i] % 14
        a[i] = 0
        j = 1
        while j <= d:
            k = (i + j) % 14
            a[k] += 1
            j += 1
        for j in range(14):
            a[j] += c
            if a[j] % 2 == 0:
                m += a[j]
        ans = max(ans, m)
    print(ans)


if __name__ == "__main__":
    # 示例调用：可修改 n 来改变生成的数据规模
    main(100)