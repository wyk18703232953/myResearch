def main(n):
    nxt = {'R': 'G', 'G': 'B', 'B': 'R'}

    # Interpret n as the number of test cases
    T = n

    # Deterministic generation of (n_i, k_i, s_i) for each test case
    # For test case i (0-based):
    #   length = 5 + (i % 10) + i
    #   k      = max(1, length // 3)
    #   s      = periodic RGB pattern
    for i in range(T):
        length = 5 + (i % 10) + i
        k = max(1, length // 3)
        s = ''.join('RGB'[j % 3] for j in range(length))

        n_i = length
        res = []
        for start in ['R', 'G', 'B']:
            mis = []
            cur = start
            # initial window
            for j in range(k):
                if s[j] != cur:
                    mis.append(1)

                else:
                    mis.append(0)
                cur = nxt[cur]
            res.append(sum(mis))
            # sliding window
            for j in range(k, n_i):
                res.append(res[-1] + int(s[j] != cur) - mis[j - k])
                if s[j] != cur:
                    mis.append(1)

                else:
                    mis.append(0)
                cur = nxt[cur]
        # print(min(res))
        pass
if __name__ == "__main__":
    main(10)