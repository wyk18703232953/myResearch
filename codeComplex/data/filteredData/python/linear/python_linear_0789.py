def main(n):
    # 解释输入结构：
    # 原程序读取：n, k 和一个长度为 n 的字符串 C
    # 这里将外部输入改为：n 控制字符串长度，k 取与 n 相关的确定性值
    # C 为长度为 n 的 01 字符串，按确定性规则生成
    if n <= 0:
        return

    # 确定性地选择 k，保证 1 <= k <= n
    # 选择一个与 n 有关的模式以生成不同情况，例如：
    # k 在 [1, n] 范围内循环变化
    k = max(1, (n // 3) if n >= 3 else 1)
    if k > n:
        k = n

    # 确定性生成长度为 n 的 01 串 C
    # 使用简单的周期模式：'0','1','0','1',...，并在特定位置翻转
    C = [('0' if i % 2 == 0 else '1') for i in range(n)]
    # 为了产生更多样的前后缀情况，在前 1/4 和后 1/4 做确定性改动
    quarter = max(1, n // 4)
    for i in range(quarter):
        C[i] = '0'
    for i in range(n - quarter, n):
        C[i] = '1'

    def JUDGE(C_local):
        ANS_one = 0
        ANS_zero = 0
        for c in C_local:
            if c == "0":
                ANS_zero += 1

            else:
                break
        for c in C_local[::-1]:
            if c == "0":
                ANS_zero += 1

            else:
                break
        for c in C_local:
            if c == "1":
                ANS_one += 1

            else:
                break
        for c in C_local[::-1]:
            if c == "1":
                ANS_one += 1

            else:
                break
        if ANS_zero >= n - k or ANS_one >= n - k:
            return 1

        else:
            return 0

    if JUDGE(C) == 1:
        # print("tokitsukaze")
        pass
        return

    if k >= n - 1:
        # print("quailty")
        pass
        return

    if k < n / 2:
        # print("once again")
        pass
        return

    CAN1 = C[:]
    CAN2 = C[:]

    if C[0] == "0":
        for i in range(1, min(k + 1, n)):
            CAN1[i] = "1"

    else:
        for i in range(1, min(k + 1, n)):
            CAN1[i] = "0"

    if C[-1] == "0":
        for i in range(n - 1, max(n - k - 1, -1), -1):
            CAN2[i] = "1"

    else:
        for i in range(n - 2, max(n - k - 2, -1), -1):
            if 0 <= i < n:
                CAN2[i] = "0"

    if JUDGE(CAN1) == 1 and JUDGE(CAN2) == 1:
        # print("quailty")
        pass
        return

    else:
        # print("once again")
        pass
        return


if __name__ == "__main__":
    # 示例调用：可以根据需要修改 n 进行规模实验
    main(10)