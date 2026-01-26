def main(n):
    A = [i // 2 for i in range(n)]
    A.sort()

    from collections import Counter
    C = Counter(A)
    dou = 0

    for c in C:
        dou += C[c] - 1

        if C[c] >= 2 and C[c - 1] != 0:
            # print("cslnb")
            pass
            return

    if dou >= 2:
        # print("cslnb")
        pass
        return

    ANS = 0
    for i in range(n):
        if A[i] < i:
            # print("cslnb")
            pass
            return
        ANS += (A[i] - i) % 2

    if ANS % 2 == 0:
        # print("cslnb")
        pass

    else:
        # print("sjfnb")
        pass
if __name__ == "__main__":
    main(10)