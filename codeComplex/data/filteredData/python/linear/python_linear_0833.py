def main(n):
    # Interpret n as the length of string s; k is derived deterministically from n
    # Also, interpret q (number of test cases) deterministically from n
    # q grows slowly with n so we can scale experiments by increasing n
    if n <= 0:
        return

    # Number of test cases
    q = max(1, n // 10)

    # Deterministic generation of (n_i, k_i, s_i) for each test case
    # For variability but determinism:
    # - n_i ranges around n
    # - k_i is in [1, n_i]
    # - s_i is a periodic pattern over 'R', 'G', 'B'
    base_n = n

    for t in range(q):
        # Generate per-test-case n and k deterministically
        n_i = base_n - (t % max(1, base_n // 4))
        if n_i <= 0:
            n_i = 1
        k_i = 1 + (t % n_i)

        # Generate string s deterministically
        # pattern cycles through 'R', 'G', 'B'
        chars = ['R', 'G', 'B']
        s = ''.join(chars[(i + t) % 3] for i in range(n_i))

        R = 0
        G = 0
        B = 0
        ans = float('inf')

        for j in range(n_i):
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

            if j >= k_i - 1:
                ans = min(ans, R, G, B)
                idx = j - k_i + 1
                if idx % 3 == 0:
                    if s[idx] == 'R':
                        G -= 1
                        B -= 1
                    elif s[idx] == 'G':
                        R -= 1
                        B -= 1

                    else:
                        R -= 1
                        G -= 1
                elif idx % 3 == 1:
                    if s[idx] == 'R':
                        G -= 1
                        R -= 1
                    elif s[idx] == 'G':
                        G -= 1
                        B -= 1

                    else:
                        R -= 1
                        B -= 1

                else:
                    if s[idx] == 'R':
                        R -= 1
                        B -= 1
                    elif s[idx] == 'G':
                        R -= 1
                        G -= 1

                    else:
                        G -= 1
                        B -= 1

        # print(ans)
        pass
if __name__ == "__main__":
    main(1000)