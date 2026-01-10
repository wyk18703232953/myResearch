def main(n):
    def testcase(n, offset):
        # Generate deterministic intervals based on n and offset
        # Each test consists of n intervals
        cnt = dict()
        for i in range(n):
            # Deterministic construction of l, r
            l = offset + i
            r = offset + i + (i % 5)
            cnt[l] = cnt.get(l, 0) + 1
            cnt[r + 1] = cnt.get(r + 1, 0) - 1

        ans = [0] * (n + 1)
        sk = sorted(cnt.keys())
        cnt_i = 0
        for ind, x in enumerate(sk[:-1]):
            cnt_i += cnt[x]
            ans[cnt_i] += sk[ind + 1] - x
        return ans[1:]

    # Simulate a single main testcase of size n
    res_single = testcase(n, 0)

    # Simulate multiple testcases: choose T = min(n, 5) for scalability
    T = n if n <= 5 else 5
    all_results = []
    for t in range(T):
        all_results.append(testcase(n, t * (n + 1)))

    # Output format: first line is single-testcase result,
    # followed by T lines of multi-testcase results
    print(" ".join(str(x) for x in res_single))
    for res in all_results:
        print(" ".join(str(x) for x in res))


if __name__ == "__main__":
    # Example call; adjust n for different input scales
    main(10)