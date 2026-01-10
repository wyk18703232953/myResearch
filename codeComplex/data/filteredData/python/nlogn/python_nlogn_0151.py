def main(n):
    # 确定性生成 n 和 k
    # n 用作数组长度，k 为固定缩放因子（>1）
    k = 3
    if n <= 0:
        print(0)
        return

    # 生成长度为 n 的整数数组 a，保证有序且可触发 x%k==0 的情况
    # 使用简单算术构造，完全确定性
    # 例如：a[i] = i * 2 + (i // 3)
    a = [i * 2 + (i // 3) for i in range(n)]
    a.sort()

    if k == 1:
        print(n)
        return

    # 将 a 转为字典，键为数值，值为索引
    a = dict(zip(a, range(n)))
    b = {}
    count = {}

    for x in a:
        if x % k == 0 and int(x / k) in a:
            b[x] = b[int(x / k)]
            count[b[int(x / k)]] += 1
        else:
            b[x] = x
            count[x] = 1

    res = n
    for _, y in count.items():
        res -= int(y / 2)

    print(res)


if __name__ == "__main__":
    # 示例调用，可根据需要调整 n 进行规模化实验
    main(10)