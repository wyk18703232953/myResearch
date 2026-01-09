def main(n):
    # n controls the length of the string C; k is chosen deterministically from n
    # Ensure n >= 2 to avoid degenerate behavior
    if n < 2:
        n = 2

    # Deterministic choice of k based on n
    # Here we choose k = n // 2 (standard scale with respect to n), but ensure 1 <= k < n
    k = max(1, min(n - 1, n // 2))

    # Deterministic generation of C as a list of '0' and '1'
    # Example pattern: C[i] = '0' if i % 3 == 0 else '1'
    C = [('0' if i % 3 == 0 else '1') for i in range(n)]

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

    if JUDGE(CAN1) == 1 and JUDGE(CAN2) == 1:
        # print("quailty")
        pass

    else:
        # print("once again")
        pass
if __name__ == "__main__":
    # Example deterministic call for complexity experiments
    main(1000)