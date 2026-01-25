def main(n):
    # 映射：n -> k 和 数组长度
    # 为了规模化实验，令数组长度为 n，k 为 1..min(10,n) 的循环
    length = n if n > 0 else 1
    k = (n % 10) + 1
    if k > length:
        k = length

    # 构造确定性数组 a：元素值在 1..100000 范围内循环
    a = [(i % 100000) + 1 for i in range(length)]

    # 原始逻辑开始
    i = 0
    d = 0
    x = -1
    y = -1
    s = [0] * (10**5 + 1)

    for j in range(len(a)):
        s[a[j]] += 1
        i += 1
        if s[a[j]] == 1:
            d += 1
        if i == 1:
            x = j + 1
        if d == k:
            y = j + 1
            break

    while k != 1 and x != -1 and s[a[x - 1]] - 1 != 0:
        s[a[x - 1]] -= 1
        x += 1

    if x == -1 or y == -1:
        x = -1
        y = -1

    print(x, y)


if __name__ == "__main__":
    main(10)