def main(n):
    # Interpret n as: number of test cases q = n
    # For each test case, deterministically construct (n_i, k_i, s_i)
    # Keep original logic unchanged for each case
    q = n
    sample = "RGB"

    for t in range(q):
        # Deterministic construction of parameters per test case
        # Let string length grow with test index
        n_i = 5 + 3 * (t + 1)
        # k_i between 1 and n_i, varying deterministically
        k_i = 1 + (t * 2) % n_i

        # Deterministic construction of s: repeat "RGB" pattern, then alter some chars
        base = (sample * ((n_i // 3) + 2))[:n_i]
        # Introduce deterministic variations
        s_list = list(base)
        for i in range(0, n_i, 4):
            # flip character in a deterministic cyclic way
            if s_list[i] == 'R':
                s_list[i] = 'G'
            elif s_list[i] == 'G':
                s_list[i] = 'B'

            else:
                s_list[i] = 'R'
        s = "".join(s_list)

        ans = k_i
        for i in range(n_i - k_i + 1):
            cnt = 0
            x = 0
            for j in range(i, i + k_i):
                if s[j] != sample[x]:
                    cnt += 1
                x = (x + 1) % 3
            ans = min(ans, cnt)

            cnt = 0
            x = 1
            for j in range(i, i + k_i):
                if s[j] != sample[x]:
                    cnt += 1
                x = (x + 1) % 3
            ans = min(ans, cnt)

            cnt = 0
            x = 2
            for j in range(i, i + k_i):
                if s[j] != sample[x]:
                    cnt += 1
                x = (x + 1) % 3
            ans = min(ans, cnt)

        # print(ans)
        pass
if __name__ == "__main__":
    main(5)