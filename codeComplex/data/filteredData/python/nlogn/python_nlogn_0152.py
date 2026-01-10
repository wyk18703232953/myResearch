def main(n):
    # 确定性生成 n 和 k
    # 让 k 在 [2, 10] 内循环变化，避免 k=1 的退化情况占主导
    if n <= 0:
        return
    k = (n % 9) + 2  # k in [2,10]

    # 生成长度为 n 的数组 a
    # 生成一些可被 k 成比例连接的数对以保留原逻辑特性
    a = []
    base = 1
    for i in range(n):
        if i % 3 == 0:
            # 构造一个 x，使得前面有可能存在 x/k
            x = (i + 1) * k
        else:
            x = i + base
        a.append(x)

    a.sort()
    a = dict(zip(a, range(n)))
    count = {}
    b = {}

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
    main(10)