import copy
import random

def JUDGE(C, n, k):
    ANS_one = 0
    ANS_zero = 0

    for c in C:
        if c == "0":
            ANS_zero += 1
        else:
            break

    for c in C[::-1]:
        if c == "0":
            ANS_zero += 1
        else:
            break

    for c in C:
        if c == "1":
            ANS_one += 1
        else:
            break

    for c in C[::-1]:
        if c == "1":
            ANS_one += 1
        else:
            break

    if ANS_zero >= n - k or ANS_one >= n - k:
        return 1
    else:
        return 0

def main(n):
    # 生成测试数据：长度为 n 的 01 串，以及 1 <= k < n
    if n < 2:
        # 对于太小的 n，我们无法生成合法的 k，直接返回
        return

    k = random.randint(1, n - 1)
    C = [random.choice(["0", "1"]) for _ in range(n)]

    if JUDGE(C, n, k) == 1:
        print("tokitsukaze")
        return

    if k >= n - 1:
        print("quailty")
        return

    if k < n / 2:
        print("once again")
        return

    CAN1 = copy.copy(C)
    CAN2 = copy.copy(C)

    if C[0] == "0":
        for i in range(1, k + 1):
            CAN1[i] = "1"
    else:
        for i in range(1, k + 1):
            CAN1[i] = "0"

    if C[-1] == "0":
        for i in range(n - 1, n - k - 1, -1):
            CAN2[i] = "1"
    else:
        for i in range(n - 2, n - k - 2, -1):
            CAN2[i] = "0"

    if JUDGE(CAN1, n, k) == 1 and JUDGE(CAN2, n, k) == 1:
        print("quailty")
    else:
        print("once again")


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)