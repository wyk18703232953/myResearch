def main(n):
    import sys
    import copy

    # Ensure n is at least 2 to make the problem meaningful
    if n < 2:
        n = 2

    # Deterministically define k based on n
    # Let k be roughly n//2 but within [1, n-1]
    k = max(1, min(n - 1, n // 2))

    # Deterministically generate C as a list of '0' and '1' of length n
    # Pattern: alternating '0' and '1'
    C = [('0' if i % 2 == 0 else '1') for i in range(n)]

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

    if JUDGE(CAN1) == 1 and JUDGE(CAN2) == 1:
        # print("quailty")
        pass

    else:
        # print("once again")
        pass
if __name__ == "__main__":
    # Example call for time-complexity experiments
    main(10)