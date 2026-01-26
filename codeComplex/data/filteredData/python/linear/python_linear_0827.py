def main(n):
    # Interpret n as:
    # q = n   (number of test cases)
    # For each test case t (0-based):
    #   k_t = t+1
    #   string length n_t = n + t
    #   S_t[i] = "R" if i % 3 == 0, "G" if i % 3 == 1, else "B"
    q = n
    results = []
    for t in range(q):
        nt = n + t
        kt = t + 1
        if kt > nt:
            kt = nt
        S = []
        for i in range(nt):
            r = i % 3
            if r == 0:
                S.append("R")
            elif r == 1:
                S.append("G")

            else:
                S.append("B")

        for i in range(nt):
            if S[i] == "R":
                S[i] = 0
            elif S[i] == "G":
                S[i] = 1

            else:
                S[i] = 2

        ANS = 1 << 50

        for mod in range(3):
            SUM = 0
            for i in range(kt):
                if S[i] % 3 != (mod + i) % 3:
                    SUM += 1

            if SUM < ANS:
                ANS = SUM

            for i in range(kt, nt):
                if S[i - kt] % 3 != (mod + (i - kt)) % 3:
                    SUM -= 1
                if S[i] % 3 != (mod + i) % 3:
                    SUM += 1
                if SUM < ANS:
                    ANS = SUM

        results.append(ANS)

    for r in results:
        # print(r)
        pass
if __name__ == "__main__":
    main(5)