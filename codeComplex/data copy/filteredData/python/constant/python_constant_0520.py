def main(n):
    # 映射规则：
    # x, y, z 在 [0, n] 范围内构造
    # t1, t2, t3 在 [1, n+1] 范围内构造
    x = 0
    y = n // 2
    z = n
    t1 = 1 + (n % 5)
    t2 = 1 + (n % 7)
    t3 = 1 + (n % 3)

    d1 = abs(x - y) * t1
    d2 = abs(x - z) * t2 + abs(x - y) * t2 + 3 * t3

    if d2 <= d1:
        # print('YES')
        pass

    else:
        # print('NO')
        pass
if __name__ == "__main__":
    main(10)