def main(n):
    # n 作为输入规模，这里生成 n 个测试用例，从 -n 到 n-1
    results = []
    for a in range(-n, n):
        x = a
        if x > 0:
            results.append(str(x))

        else:
            x = x - 2 * x  # 绝对值
            k = x // 10
            b = x % 10
            c = (x // 100) * 10 + b
            if k < c:
                if k != 0:
                    results.append("-%d" % k)

                else:
                    results.append(str(k))

            else:
                if c != 0:
                    results.append("-%d" % c)

                else:
                    results.append(str(c))
    # 为了使程序输出可见，这里将所有结果逐行打印
    for r in results:
        # print(r)
        pass
if __name__ == "__main__":
    main(10)