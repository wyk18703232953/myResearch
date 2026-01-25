def main(n):
    # 映射规则：
    # - 节点数 = n（若 n < 2，则调整为 2，保证至少一条边）
    # - s = n 的平方，随规模单调增长
    # - 构造一棵链状树：1-2-3-...-n，便于规模可控且确定
    if n < 2:
        n = 2

    s = n * n  # 确定性构造的 s

    # 模拟原程序逻辑
    d = [0] * (n + 1)
    cnt = 0

    # 构造 n-1 条边，形成一条链
    for i in range(0, n - 1):
        a = i + 1
        b = i + 2
        d[a - 1] += 1
        d[b - 1] += 1

    for i in range(0, n):
        if d[i] == 1:
            cnt += 1

    result = 2.0 * s / cnt
    print(result)
    return result


if __name__ == "__main__":
    # 示例调用，可根据需要更改 n 来做规模实验
    main(10)