def main(n: int) -> int:
    # 根据 n 生成测试数据，这里令 k = n（可按需要修改生成规则）
    k = n

    limit = 998244353

    if k > 2 * n:
        return 0
    elif k == 1 or k == 2 * n:
        return 2

    else:
        same = [0] * (k + 1)
        same[1] = 2

        diff = [0] * (k + 1)
        diff[2] = 2

        for i in range(2, n + 1):
            for j in range(min(k, 2 * i), 1, -1):
                same[j] = same[j] + 2 * diff[j] + same[j - 1]
                same[j] %= limit

                diff[j] = diff[j] + 2 * same[j - 1] + diff[j - 2]
                diff[j] %= limit

        return (same[k] + diff[k]) % limit


if __name__ == "__main__":
    # 示例：调用 main(10) 并打印结果
    # print(main(10))
    pass