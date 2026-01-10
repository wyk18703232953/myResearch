def main(n):
    # 为了保持原程序的“三个整数 + n 个整数数组”的输入结构，
    # 这里将 n 既作为数组长度，又由它确定 a, b 的取值。
    # 生成确定性的 a, b
    if n < 2:
        # 至少需要 2 个元素才能分成两组
        n_effective = 2
    else:
        n_effective = n

    # 让 a, b 满足 0 <= a < b <= n_effective
    a = n_effective // 3
    b = (2 * n_effective) // 3
    if b == a:
        b = min(a + 1, n_effective)

    # 生成确定性的高度数组 h_raw，长度为 n_effective
    # 使用简单的算术构造：h[i] = (i * 3 + 1) // 2
    h_raw = [(i * 3 + 1) // 2 for i in range(n_effective)]

    # 保持原程序逻辑
    h = sorted(h_raw)
    Vasya = h[:b]
    Petya = h[b:]
    # 当 b == n_effective 时，Petya 为空，避免索引错误
    if not Petya or not Vasya:
        result = 0
    else:
        result = Petya[0] - Vasya[-1]

    print(result)


if __name__ == "__main__":
    main(10)