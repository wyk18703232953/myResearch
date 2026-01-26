def main(n):
    # 将 n 解释为题目中的题目数量规模
    # 构造参数：n, l, r, x, c[]
    # 这里构造一个确定性的 c 列表，以及 l, r, x
    global c, l, r, x

    # 确定性构造难度数组 c：严格递增，长度为 n
    # 例如 c[i] = (i + 1) * 3
    c = [(i + 1) * 3 for i in range(n)]
    c.sort()

    # 构造 l, r, x 为与 n 有关的确定性值
    # 总和范围 [l, r] 覆盖一部分子集
    total_sum = sum(c)
    l = total_sum // 4
    r = total_sum // 2
    x = max(3, n // 2)  # 差值阈值

    def func():
        count = 0
        for i in range(1 << n):
            temp = []
            for j in range(n):
                if (1 << j) & i:
                    temp.append(c[j])

            if temp and l <= sum(temp) <= r and temp[-1] - temp[0] >= x:
                count += 1
        print(count)

    func()


if __name__ == "__main__":
    main(10)