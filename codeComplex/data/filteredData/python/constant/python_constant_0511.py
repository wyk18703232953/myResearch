def main(n):
    # 生成 n 组测试数据 (x, y, k)
    # 规模含义：n 为测试用例数量
    results = []
    for q in range(n):
        x = q
        y = (q * 2) % (n + 3)
        k = (q * 3 + 5) % (n + 7) + max(x, y)
        if max(x, y) > k:
            results.append(-1)

        else:
            if (x + y) % 2 == 0:
                if k % 2 == max(x, y) % 2:
                    results.append(k)

                else:
                    results.append(k - 2)

            else:
                results.append(k - 1)
    # 输出结果，保持与原程序行为类似（逐行打印）
    for r in results:
        # print(r)
        pass
if __name__ == "__main__":
    main(10)