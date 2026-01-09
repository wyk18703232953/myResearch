def main(n: int):
    # 生成测试数据：根据规模 n 构造一个合适的 k
    # 这里示例取 k = n（保证一般情况，且避免明显退化到边界）
    k = n

    limit = 998244353

    if k > 2 * n:
        # print(0)
        pass
        return
    elif k == 1 or k == 2 * n:
        # print(2)
        pass
        return

    else:
        same = [0] * (k + 1)
        same[1] = 2

        diff = [0] * (k + 1)
        if k >= 2:
            diff[2] = 2

        for i in range(2, n + 1):
            upper = min(k, 2 * i)
            for j in range(upper, 1, -1):
                same[j] = same[j] + 2 * diff[j] + same[j - 1]
                same[j] %= limit

                if j >= 2:
                    diff[j] = diff[j] + 2 * same[j - 1] + diff[j - 2]
                    diff[j] %= limit

        # print((same[k] + diff[k]) % limit)
        pass
if __name__ == "__main__":
    # 示例：调用 main(10) 进行运行
    main(10)