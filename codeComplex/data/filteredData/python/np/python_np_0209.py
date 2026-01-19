def main(n):
    # 参数含义：
    # n: 题目中原本的题目数量（数组长度）
    #
    # 为了构造完全确定性的输入，映射规则如下：
    # l = n * 2
    # r = n * (n + 1) // 2  （相当于 1..n 的和）
    # x = max(1, n // 3)
    # C 为长度为 n 的数组：C[i] = i + 1
    #
    # 这样随 n 增大，数组长度和数值规模都随之增大，可以用于时间复杂度实验。

    if n <= 0:
        print(0)
        return

    l = n * 2
    r = n * (n + 1) // 2
    x = max(1, n // 3)
    C = list(range(1, n + 1))

    ANS = 0
    for i in range(2 ** n):
        s = bin(i)[2:]
        s = '0' * (n - len(s)) + s
        L = []
        for j in range(n):
            if s[j] == '1':
                L.append(C[j])
        if len(L) < 2 or not (l <= sum(L) <= r) or L[-1] - L[0] < x:
            continue
        ANS += 1
    print(ANS)


if __name__ == "__main__":
    main(10)