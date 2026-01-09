def main(n):
    # 映射规则：
    # n -> 输入规模
    # 1) T = n
    # 2) ts 为长度为 n 的确定性数组：ts[i] = i % (n + 1)
    # 3) 设定 a, b, c 为与 n 相关但确定性的值
    T = n
    a = 2 * n + 1
    b = n // 2 + 1
    c = n % 5 + 1

    ts = [i % (n + 1) for i in range(n)]
    ts.sort()

    ans = 0
    for t in ts:
        temp = -10**18
        for u in range(t, T + 1):
            temp = max(temp, c * (u - t) + a - b * (u - t))
        ans += temp
    # print(ans)
    pass
if __name__ == "__main__":
    main(1000)