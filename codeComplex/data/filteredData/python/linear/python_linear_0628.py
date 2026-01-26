def main(n):
    # n 表示测试用例数量
    t = n

    for ca in range(t):
        # 为第 ca 个用例确定性生成 (n, k)
        # 这里将 n 映射为规模，k 为随规模增长的阈值
        case_n = ca + 1  # 从 1 开始递增
        case_k = (case_n * case_n * (ca + 2)) // 2 + 1

        if case_n >= 40:
            # print("YES " + str(case_n - 1))
            pass

        else:
            ans = -1
            for m in range(1, case_n + 1):
                asd = (4 ** m - 1) // 3
                asd2 = (2 ** m - 1) ** 2
                asd2 *= (4 ** (case_n - m) - 1) // 3
                asd += asd2
                if asd >= case_k and m * m <= case_k:
                    ans = case_n - m
                    break
            if ans == -1:
                # print("NO")
                pass

            else:
                # print("YES " + str(ans))
                pass
if __name__ == "__main__":
    main(5)