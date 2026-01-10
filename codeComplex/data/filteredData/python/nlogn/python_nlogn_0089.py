def main(n):
    # 映射含义：
    # n -> 原题中的 n（学生数量）
    # a 和 b 由 n 确定性生成
    # h 为长度为 n 的身高数组，确定性构造后排序

    if n < 2:
        # 至少需要两个学生才能计算差值
        print(0)
        return

    # 确定性生成 a, b，保证 1 <= a < b < n
    # 这里让 a 接近 n/4，b 接近 n/2，但限定在合法范围内
    a = max(1, n // 4)
    b = max(a + 1, n // 2)
    if b >= n:
        b = n - 1
        if a >= b:
            a = b - 1

    # 确定性生成身高数组 h，长度为 n
    # 使用简单算术构造，随后排序
    h = [(i * 3 + 7) % (2 * n + 5) + (i // 2) for i in range(n)]
    h.sort()

    print(h[b] - h[b - 1])


if __name__ == "__main__":
    # 示例调用：可以根据需要更改 n 的值做规模实验
    main(10)