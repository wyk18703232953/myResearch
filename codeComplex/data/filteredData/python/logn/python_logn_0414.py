def main(n):
    # 这里根据 n 生成一组或多组 (n, k) 测试数据。
    # 为了演示：生成 t = n 组测试，每组 n 固定为当前 n，k 从 0 到 n-1。
    t = n
    test_cases = []
    for k in range(t):
        test_cases.append((n, k))

    # 正式逻辑开始
    for n_case, k in test_cases:
        n = n_case
        if n >= 50:
            if k == 0:
                # print("YES " + str(n))
                pass

            else:
                # print("YES " + str(n - 1))
                pass

        else:
            a = [0] * (n + 1)
            b = [0] * (n + 1)
            c = [0] * (n + 1)
            a[0] = 0
            b[n] = 1
            c[n] = 0

            for i in range(1, n + 1):
                a[i] = 4 * a[i - 1] + 1
            for i in range(n - 1, -1, -1):
                b[i] = b[i + 1] * 2 + 1
            for i in range(n - 1, -1, -1):
                c[i] = c[i + 1] + b[i + 1]

            res = -1
            for d in range(n + 1):
                if c[d] <= k and k <= a[n] - a[d] * b[d]:
                    res = d

            if res == -1:
                # print("NO")
                pass

            else:
                # print("YES " + str(res))
                pass
if __name__ == "__main__":
    # 示例调用：规模 n = 10
    main(10)