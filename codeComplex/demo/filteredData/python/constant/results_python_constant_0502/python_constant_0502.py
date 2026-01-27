def main(n):
    # n 表示查询数量 q
    q = n
    results = []
    for i in range(q):
        # 确定性生成 (x, y, k)
        # 随规模 n 线性增长，保证多样性并覆盖多种情况
        k = i + 1
        x = (2 * i) % (k + 1)
        y = (3 * i) % (k + 1)

        if x > k or y > k:
            results.append(-1)

        else:
            if (x + y) % 2 == 0:
                if (k - max(x, y)) % 2 == 0:
                    results.append(k)

                else:
                    results.append(k - 2)

            else:
                if (k - max(x, y)) % 2 == 0:
                    results.append(k - 1)

                else:
                    results.append(k - 1)

    # 输出以便在实验环境中有可见结果
    for r in results:
        # print(r)
        pass
if __name__ == "__main__":
    main(10)