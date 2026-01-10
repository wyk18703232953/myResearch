def main(n):
    # 确定性构造 K
    K = n // 3 + 1  # 保证 K >= 1，随 n 线性变化

    # 确定性构造长度为 n 的数组 b
    # 构造方式：包含重复和间隔变化
    # b[i] = (i // 2) % (K + 3) + (i // (K + 1))
    b = [((i // 2) % (K + 3) + (i // (K + 1))) for i in range(n)]

    b.sort()
    l = 0
    cur = 0
    for i in range(1, n):
        if b[i] == b[i - 1]:
            continue
        if b[i] > b[i - 1] + K:
            l = i
        else:
            cur += (i - l)
            l = i
    print(n - cur)


if __name__ == "__main__":
    main(10)