def main(n):
    # 确定性生成 k 和数组 a，规模由 n 控制
    if n <= 0:
        return

    # 令数组长度为 n，元素值为 i % max(1, n//3)，保证有重复元素结构
    a = [i % max(1, n // 3) for i in range(n)]
    # 令 k 与 n 成线性关系，保证可扩展
    k = n * 5

    d = {}
    for chr in a:
        if chr not in d:
            d[chr] = 1
        else:
            d[chr] += 1

    p = list(d.values())
    z = k // n
    if z == 0:
        print(0)
    else:
        o = []
        if len(a) >= n:
            o.append(1)
        for i in range(2, z + 1):
            c = 0
            for j in range(len(p)):
                c += p[j] // i
            if c >= n:
                o.append(i)
        print(max(o))


if __name__ == "__main__":
    # 示例：可以调整此处的 n 进行规模化实验
    main(10)