def main(n):
    # 生成测试数据
    # info[0] = 元素个数，info[1] = 容量限制
    m = n                          # 元素个数
    k = max(1, n // 3)             # 容量限制，示例策略：大约为 n/3
    info = [m, k]

    # 构造 powers 和 coins，示例：简单的线性数据
    # powers: 1..m
    # coins: m..1
    powers = list(range(1, m + 1))
    coins = list(range(m, 0, -1))

    # 原始逻辑
    l = sorted(zip(powers, coins, range(info[0])))
    final = [0] * info[0]
    s = 0
    w = []
    for _, c, i in l:
        s += c
        final[i] = s
        w = sorted(w + [c])
        if len(w) > info[1]:
            s -= w[0]
            del w[0]

    # print(*final)
    pass
if __name__ == "__main__":
    # 示例：调用 main(5) 进行测试
    main(5)