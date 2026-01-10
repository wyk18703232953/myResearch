def main(n):
    # 规模含义：
    # n = 数组长度
    # 构造确定性的 k 和数组 a
    if n <= 1:
        # 边界情况：长度不足
        print(0)
        return

    # 将 k 设置为与 n 相关的确定性值，保证 1 <= k <= n
    # 这里取 k = n // 3 + 1，且不超过 n
    k = n // 3 + 1
    if k > n:
        k = n

    # 构造一个确定性的非降序数组 a，保证差分非负
    # 例如：a[i] = i * 2 + (i // 3)
    a = [i * 2 + (i // 3) for i in range(n)]

    if k == 1:
        print(max(a) - min(a))
        return

    dif = []
    for i in range(n - 1):
        dif.append(a[i + 1] - a[i])
    dif = sorted(dif)
    print(sum(dif[:-k + 1]))


if __name__ == "__main__":
    # 示例调用：可修改 n 以进行规模化实验
    main(10)