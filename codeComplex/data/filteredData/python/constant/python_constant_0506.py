def main(n):
    # 解释规模映射：
    # n 表示测试用例数量 q
    # 每个用例 (n_i, m_i, k_i) 由 i 确定性生成
    Q = []
    for i in range(1, n + 1):
        ni = i
        mi = i + 1
        ki = 2 * i + 1
        Q.append([ni, mi, ki])

    results = []
    for ni, mi, ki in Q:
        if ni > ki or mi > ki:
            results.append(-1)
            continue

        x = max(ni, mi) - min(ni, mi)
        y = ki - max(ni, mi)

        if x % 2 == 0 and y % 2 == 0:
            results.append(ki)
        elif x % 2 == 0 and y % 2 == 1:
            results.append(ki - 2)
        elif x % 2 == 1 and y % 2 == 0:
            results.append(ki - 1)
        elif x % 2 == 1 and y % 2 == 1:
            results.append(ki - 1)

    # 为了在复杂度实验中减少 IO 开销，统一一次性输出
    for r in results:
        # print(r)
        pass
if __name__ == "__main__":
    main(10)