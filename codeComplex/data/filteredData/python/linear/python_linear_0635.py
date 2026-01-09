def main(n: int):
    """
    将原逻辑封装为 main(n)，并根据 n 自动生成测试数据。
    这里生成 t = n 组测试，每组的 (n_i, k_i) 按以下规则：
      - n_i = i + 1
      - k_i = i * i
    你可以根据需要修改测试数据生成方式。
    """
    t = n  # 测试组数由规模 n 决定

    for i in range(t):
        ni = i + 1          # 第 i 组的 n
        ki = i * i          # 第 i 组的 k，可按需求调整

        n_case = ni
        k = ki

        if n_case >= 50:
            if k == 0:
                # print("YES " + str(n_case))
                pass

            else:
                # print("YES " + str(n_case - 1))
                pass

        else:
            a = [0] * (n_case + 1)
            b = [0] * (n_case + 1)
            c = [0] * (n_case + 1)
            a[0] = 0
            b[n_case] = 1
            c[n_case] = 0

            for j in range(1, n_case + 1):
                a[j] = 4 * a[j - 1] + 1
            for j in range(n_case - 1, -1, -1):
                b[j] = b[j + 1] * 2 + 1
            for j in range(n_case - 1, -1, -1):
                c[j] = c[j + 1] + b[j + 1]

            res = -1
            for d in range(n_case + 1):
                if c[d] <= k and k <= a[n_case] - a[d] * b[d]:
                    res = d

            if res == -1:
                # print("NO")
                pass

            else:
                # print("YES " + str(res))
                pass


# 示例：直接运行时可以调用 main
if __name__ == "__main__":
    main(10)