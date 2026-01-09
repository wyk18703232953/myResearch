def main(n):
    # 映射：将 n 映射为区间 [l, r]
    # 这里令 l = 1，r = n + 2，保证当 n >= 1 时一定能找到三元组
    l = 1
    r = n + 2

    a, b, c = l, l + 1, l + 2

    if l % 2 != 0:
        a, b, c = a + 1, b + 1, c + 1

    if c > r:
        # print(-1)
        pass

    else:
        # print(a, b, c)
        pass
if __name__ == "__main__":
    main(10)