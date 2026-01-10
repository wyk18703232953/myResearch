def main(n):
    # 映射：给定 n，构造 n 和 k 以及 n 行数据
    # 设 k = n // 2 + 1，保证 1 <= k <= n
    if n <= 0:
        return
    k = n // 2 + 1

    # 构造 ais，为 n 行，每行两个整数
    # 保证存在重复项，便于 count
    # 第一个元素从 n 到 1，第二个元素为 i % 3
    ais = []
    for i in range(n):
        first = n - i
        second = i % 3
        ais.append([first, second])

    ais.sort(key=lambda x: (-x[0], x[1]))
    print(ais.count(ais[k - 1]))


if __name__ == "__main__":
    main(10)