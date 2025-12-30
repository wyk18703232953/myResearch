def main(n):
    # n 为规模参数，这里用来生成多个测试样例：k = 1, 2, ..., n
    # 原程序是求第 k 位数字（基于某种特殊构造），这里对每个 k 运行一次
    T = (
        0,
        9,
        189,
        2889,
        38889,
        488889,
        5888889,
        68888889,
        788888889,
        8888888889,
        98888888889,
        1088888888889,
    )

    results = []
    for k in range(1, n + 1):
        a = 0
        for i in T:
            if i - k > 0:
                a = T.index(i)
                break
        temp = T[a] - k
        x = temp % a
        res = (10 ** a) - 1 - int(temp / a)
        ans = int((res % (10 ** (x + 1))) / (10 ** x))
        results.append(ans)

    # 输出所有结果，每个k对应一个答案
    for v in results:
        print(v)


if __name__ == "__main__":
    # 示例：运行规模 n = 20
    main(20)