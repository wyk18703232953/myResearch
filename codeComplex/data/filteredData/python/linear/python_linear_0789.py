import copy

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
    if n <= 1:
        return
    k = n // 2
    C = [str((i // 2) % 2) for i in range(n)]
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
            CAN2[i] = "0"
    if JUDGE(CAN1, n, k) == 1 and JUDGE(CAN2, n, k) == 1:
        print("quailty")
        return
    else:
        print("once again")
        return

if __name__ == "__main__":
    main(10)