def main(n):
    from collections import Counter

    # 生成确定性输入：
    # n: 节点数量（≥2）
    # s: 总权值，设为 n 的平方，随规模单调增长
    if n < 2:
        n = 2

    s = n * n

    # 构造一棵确定性的树：链式结构 1-2-3-...-n
    d = Counter()
    for i in range(1, n):
        u, v = i, i + 1
        d[u] += 1
        d[v] += 1

    l = sum(v == 1 for v in d.values())
    ans = s / l * 2
    print('%.10f' % ans)


if __name__ == "__main__":
    # 示例调用，可按需要修改 n 以进行规模实验
    main(10)