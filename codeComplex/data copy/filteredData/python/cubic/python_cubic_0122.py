def problem(s, p):
    for i in range(len(p)):
        l = p[:i] + ' '
        r = p[i:] + ' '

        dp = [0] + [None] * i

        for x in s:
            for j in range(i, -1, -1):
                if dp[j] is None:
                    continue

                if l[j] == x:
                    dp[j + 1] = dp[j] if dp[j + 1] is None else max(dp[j], dp[j + 1])

                if r[dp[j]] == x:
                    dp[j] += 1

        if dp[-1] == len(r) - 1:
            return 'YES'

    return 'NO'


def main(n):
    # n: number of test cases; also controls string sizes deterministically
    results = []
    for t in range(n):
        # Generate deterministic strings s and p based on t and n
        # Alphabet: lowercase letters
        s_len = max(1, (t + 1) * 2)
        p_len = max(1, (t % 5) + 1)

        s = ''.join(chr(ord('a') + (i + t) % 26) for i in range(s_len))
        p = ''.join(chr(ord('a') + (i * 2 + t) % 26) for i in range(p_len))

        res = problem(s, p)
        results.append(res)

    # Output all results, one per line
    for r in results:
        # print(r)
        pass
if __name__ == "__main__":
    main(5)