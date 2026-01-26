def main(n):
    # n controls: number of test cases = n, each with string length = n and window size k = max(1, n//2)
    q = n
    k = max(1, n // 2)

    for testcases in range(q):
        # Deterministically generate a string S of length n over 'R', 'G', 'B'
        chars = ['R', 'G', 'B']
        S = []
        for i in range(n):
            S.append(chars[(i + testcases) % 3])

        # Convert characters to numeric representation
        for i in range(n):
            if S[i] == "R":
                S[i] = 0
            elif S[i] == "G":
                S[i] = 1

            else:
                S[i] = 2

        ANS = 1 << 50

        # Core algorithm
        for mod in range(3):
            SUM = 0
            upper = k if k <= n else n
            for i in range(upper):
                if S[i] % 3 != (mod + i) % 3:
                    SUM += 1

            ANS = min(ANS, SUM)

            for i in range(k, n):
                if S[i - k] != (mod + (i - k)) % 3:
                    SUM -= 1
                if S[i] != (mod + i) % 3:
                    SUM += 1
                ANS = min(ANS, SUM)

        # print(ANS)
        pass
if __name__ == "__main__":
    main(10)