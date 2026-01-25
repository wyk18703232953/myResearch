def main(n):
    # n 表示数组长度
    if n < 3:
        print("NO")
        return

    # 确定性生成测试数据：简单的“山峰”结构
    # 先严格递增到中间，再严格递减，保证只有一个极大值
    mid = n // 2
    a = [i for i in range(1, mid + 2)]
    a += [mid + 1 - i for i in range(1, n - mid)]

    c = 0

    for i in range(1, n - 1):
        if a[i] > a[i - 1] and a[i] > a[i + 1]:
            c += 1
        if a[i] == a[i - 1] or a[i] == a[i + 1]:
            print('NO')
            return
        if a[i] <= a[i - 1] and a[i] <= a[i + 1]:
            print('NO')
            return
    if c > 1:
        print('NO')
    else:
        print('YES')


if __name__ == "__main__":
    main(10)