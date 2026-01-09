def main(n):
    # Interpret n as the number of test cases
    test = n
    results = []

    for tests in range(test):
        # Deterministically generate S and t based on tests and n
        # S length and t length grow with n to allow scaling
        len_s = max(1, (tests + 1) * 2)
        len_t = max(1, (tests + 1))

        # Generate S as a repeating pattern of 'a'..'z'
        S = ''.join(chr(ord('a') + (i % 26)) for i in range(len_s))

        # Generate t as a shifted pattern depending on tests
        t = ''.join(chr(ord('a') + ((i + tests) % 26)) for i in range(len_t))

        LENS = len(S)
        LENT = len(t)
        flag = 0

        for i in range(1, LENT + 1):
            t1 = t[:i]
            t2 = t[i:]

            DP = [-1] * (len(t1) + 1)
            DP[0] = 0

            for s in S:
                for j in range(len(t1), -1, -1):
                    if 0 <= DP[j] < len(t2) and s == t2[DP[j]]:
                        DP[j] += 1

                    if j > 0 and s == t1[j - 1]:
                        if DP[j - 1] > DP[j]:
                            DP[j] = DP[j - 1]

            if DP[-1] == len(t2):
                results.append("YES")
                flag = 1
                break

        else:
            results.append("NO")

    for r in results:
        # print(r)
        pass
if __name__ == "__main__":
    main(5)