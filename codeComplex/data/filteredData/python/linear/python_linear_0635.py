def main(n):
    # 生成 t 和每组 (n_i, k_i) 的确定性测试数据
    t = n if n > 0 else 1
    results = []
    for it in range(t):
        # 让每组的 n_i 在 [1, max(1, 2*n)] 内循环变化
        ni = (it % (2 * n + 1)) + 1 if n > 0 else 1
        # 构造一个与 a[ni] 规模同阶的 k_i，保证可重复
        # k_i 在 0 到 (4^ni - 1) 之间循环（通过等比数列公式）
        a_ni = (4 ** ni - 1) // 3
        if a_ni <= 0:
            ki = 0

        else:
            ki = (it * it) % (a_ni + 1)

        if ni >= 50:
            if ki == 0:
                results.append("YES " + str(ni))

            else:
                results.append("YES " + str(ni - 1))

        else:
            a = [0] * (ni + 1)
            b = [0] * (ni + 1)
            c = [0] * (ni + 1)
            a[0] = 0
            b[ni] = 1
            c[ni] = 0

            for i in range(1, ni + 1):
                a[i] = 4 * a[i - 1] + 1
            for i in range(ni - 1, -1, -1):
                b[i] = b[i + 1] * 2 + 1
            for i in range(ni - 1, -1, -1):
                c[i] = c[i + 1] + b[i + 1]

            res = -1
            for d in range(ni + 1):
                if c[d] <= ki and ki <= a[ni] - a[d] * b[d]:
                    res = d

            if res == -1:
                results.append("NO")

            else:
                results.append("YES " + str(res))
    for line in results:
        # print(line)
        pass
if __name__ == "__main__":
    main(10)