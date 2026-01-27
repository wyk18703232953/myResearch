def main(n):
    # 映射 n -> 三个正整数 k1, k2, k3（确定性构造）
    # 保证三者都在 1..n+2 内，且不为 0
    if n < 1:
        n = 1
    k1 = n
    k2 = n // 2 + 1
    k3 = n // 3 + 2

    a = [k1, k2, k3]
    a = sorted(a)

    dp = [0] * 5001
    dp[0] = 1

    i = 0
    while i <= 5000:
        if dp[i] == 0 and i + a[0] <= 5000:
            while i + a[0] <= 5000:
                dp[i] = 1
                i = i + a[0]

        else:
            i += 1

    i = 0
    while i <= 5000:
        if dp[i] == 0 and i + a[1] <= 5000:
            while i + a[1] <= 5000:
                dp[i] = 1
                i = i + a[1]

        else:
            i += 1

    i = 0
    while i <= 5000:
        if dp[i] == 0 and i + a[2] <= 5000:
            while i + a[2] <= 5000:
                dp[i] = 1
                i = i + a[2]

        else:
            i += 1

    dp = dp[:2002]
    if dp.count(0) == 0:
        # print("YES")
        pass

    else:
        # print("NO")
        pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 以做规模实验
    main(10)