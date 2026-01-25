def main(n):
    # 根据 n 构造确定性的 n, m, a, b
    # 这里令 m = n，a 和 b 的长度均为 n
    m = n

    # 构造数组 a 和 b，保证完全确定性
    # a 为 0 到 n-1
    a = [i for i in range(n)]
    # b 为 (i * 2) % max(1, n) 形式，保证规模与 n 一致
    if n > 0:
        b = [(i * 2) % n for i in range(n)]
    else:
        b = []

    # 保持原算法逻辑不变
    for i in a:
        if i in b:
            print(i, end=' ')


if __name__ == "__main__":
    # 示例：以 n = 10 运行
    main(10)