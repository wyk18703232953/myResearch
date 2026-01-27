def main(n):
    # 映射 n 为 6 个整数 x, y, z, t1, t2, t3
    # 通过简单确定性规则生成
    x = n
    y = n // 2
    z = (n * 3) // 4
    t1 = (n % 5) + 1
    t2 = (n % 7) + 1
    t3 = (n % 3) + 1

    dp = abs(x - y) * t1
    dl = abs(x - z) * t2 + abs(x - y) * t2 + 3 * t3

    if dp < dl:
        # print("NO")
        pass

    else:
        # print("YES")
        pass
if __name__ == "__main__":
    main(10)