def main(n):
    # 输入结构分析：
    # 原程序读入：
    #   n
    #   l: 长度为 n 的整数排列（1~n 的某种顺序）
    #
    # 为了做可重复的规模化实验，这里：
    #   - 使用 n 作为规模参数
    #   - 生成一个确定性的排列 l
    # 生成策略（完全确定性、可重复）：
    #   l[i] = (i * 7 + 3) % n + 1
    #   若出现重复或未覆盖 1..n，则回退为顺序排列 1..n

    if n <= 0:
        return ""

    l = [(i * 7 + 3) % n + 1 for i in range(n)]
    # 检查是否为 1..n 的排列
    if len(set(l)) != n:
        l = list(range(1, n + 1))

    # 原始算法逻辑保持不变
    p = [0] * n
    for i in range(n):
        p[l[i] - 1] = i

    res = ['?'] * n

    for e in range(n, 0, -1):
        i = p[e - 1]
        res[i] = 'B'
        for j in range(i % e, n, e):
            if i != j and l[i] <= l[j] and res[j] == 'B':
                res[i] = 'A'
                break

    result = ''.join(res)
    print(result)
    return result


if __name__ == "__main__":
    # 示例：使用一个固定的 n 调用，用于规模化实验可自行修改
    main(10)