def main(n):
    # Interpret n as the length of the string s.
    # We will run a single test case (q = 1) and choose k deterministically from n.
    # For scalability testing, k is set to max(1, n // 2).
    q = 1

    # Generate deterministic test cases based solely on n
    results = []
    for _ in range(q):
        length = n
        if length <= 0:
            results.append(0)
            continue

        # Deterministically choose k relative to n, ensuring 1 <= k <= n
        k = max(1, length // 2)

        # Deterministically generate string s of length n over 'R', 'G', 'B'
        # Pattern: cycle over "RGB"
        chars = ['R', 'G', 'B']
        s = ''.join(chars[i % 3] for i in range(length))

        R = G = B = 0
        ans = float('inf')

        for j in range(length):
            if j % 3 == 0:
                if s[j] == 'R':
                    G += 1
                    B += 1
                elif s[j] == 'G':
                    R += 1
                    B += 1

                else:
                    R += 1
                    G += 1
            elif j % 3 == 1:
                if s[j] == 'R':
                    G += 1
                    R += 1
                elif s[j] == 'G':
                    G += 1
                    B += 1

                else:
                    R += 1
                    B += 1

            else:
                if s[j] == 'R':
                    R += 1
                    B += 1
                elif s[j] == 'G':
                    R += 1
                    G += 1

                else:
                    G += 1
                    B += 1

            if j >= k - 1:
                ans = min(ans, R, G, B)
                start = j - k + 1
                if start % 3 == 0:
                    if s[start] == 'R':
                        G -= 1
                        B -= 1
                    elif s[start] == 'G':
                        R -= 1
                        B -= 1

                    else:
                        R -= 1
                        G -= 1
                elif start % 3 == 1:
                    if s[start] == 'R':
                        G -= 1
                        R -= 1
                    elif s[start] == 'G':
                        G -= 1
                        B -= 1

                    else:
                        R -= 1
                        B -= 1

                else:
                    if s[start] == 'R':
                        R -= 1
                        B -= 1
                    elif s[start] == 'G':
                        R -= 1
                        G -= 1

                    else:
                        G -= 1
                        B -= 1

        results.append(ans)

    # For experimental purposes, print the result(s)
    for res in results:
        # print(res)
        pass
if __name__ == "__main__":
    # Example deterministic call for scalability/time-complexity experiments
    main(10**5)