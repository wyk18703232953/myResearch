def main(n):
    # n 作为规模参数，这里映射为 N，即数组长度
    N = max(1, n)

    # 为了保持算法逻辑不变，这里构造一个“自洽”的 L、R、C
    # 生成一个确定性的 C，使得所有 C[i] > 0，避免早期退出
    C = [i % 7 + 1 for i in range(N)]

    # 按题意从 C 反推 L、R：
    # L[i] = 左边严格大于 C[i] 的个数
    # R[i] = 右边严格大于 C[i] 的个数
    L = [0] * N
    R = [0] * N
    for i in range(N):
        l = 0
        r = 0

        j = i - 1
        while j >= 0:
            if C[j] > C[i]:
                l += 1
            j -= 1

        j = i + 1
        while j < N:
            if C[j] > C[i]:
                r += 1
            j += 1

        L[i] = l
        R[i] = r

    # 为了与原程序结构保持一致，重新计算 C_calc 并进行同样的校验流程
    C_calc = [N - L[i] - R[i] for i in range(N)]

    ok = True
    for i in range(N):
        if C_calc[i] <= 0:
            print("NO")
            ok = False
            break

        l = 0
        r = 0

        j = i - 1
        while j >= 0:
            if C_calc[j] > C_calc[i]:
                l += 1
            j -= 1

        j = i + 1
        while j < N:
            if C_calc[j] > C_calc[i]:
                r += 1
            j += 1

        if L[i] != l or R[i] != r:
            print("NO")
            ok = False
            break

    if ok:
        print("YES")
        for i in range(0, N - 1):
            print(C_calc[i], end=" ")
        print(C_calc[N - 1])


if __name__ == "__main__":
    main(10)