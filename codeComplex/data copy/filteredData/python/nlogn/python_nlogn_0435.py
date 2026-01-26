def main(n):
    # 生成测试数据：这里简单生成前 n 个正整数作为数组
    # 如需其他生成方式，可自行修改
    arr = list(range(1, n + 1))

    # 预计算 2 的幂，直到大于 10^18 为止
    p = []
    i = 0
    while 2 ** i <= 10 ** 18:
        p.append(2 ** i)
        i += 1

    # 统计每个元素出现的次数
    d = {}
    s1 = set()
    for x in arr:
        s1.add(x)
        if x not in d:
            d[x] = 1

        else:
            d[x] += 1

    # 找到无法与数组中另一元素组成 2 的幂和的数
    s2 = set()
    for val in s1:
        flag = False
        for pw in p:
            x = pw - val
            k = d.get(x, -1)
            if k != -1:
                if x == val and d[val] == 1:
                    continue

                else:
                    flag = True
                    break
        if not flag:
            s2.add(val)

    res = 0
    for val in s2:
        res += d[val]

    # print(res)
    pass
if __name__ == "__main__":
    # 示例运行：可修改参数测试不同规模
    main(10)