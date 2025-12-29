def main(n: int):
    limit = 998244353

    # 根据规模 n 生成测试数据，这里简单设定 k = n
    k = n

    if k > 2 * n:
        ans = 0
    elif k == 1 or k == 2 * n:
        ans = 2
    else:
        same = [0] * (k + 1)
        same[1] = 2

        diff = [0] * (k + 1)
        diff[2] = 2

        for i in range(2, n + 1):
            upper = min(k, 2 * i)
            for j in range(upper, 1, -1):
                same[j] = same[j] + 2 * diff[j] + same[j - 1]
                same[j] %= limit

                diff[j] = diff[j] + 2 * same[j - 1] + diff[j - 2]
                diff[j] %= limit

        ans = (same[k] + diff[k]) % limit

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)