def main(n):
    # Deterministically generate test cases based on n
    # Interpret n as both:
    # - number of test cases T = n
    # - string length and window size derived from n for each test
    
    T = n
    results = []
    for t in range(1, T + 1):
        # For each test, define:
        # n_t: length of string
        # k_t: window size (1 <= k_t <= n_t)
        # Make them depend deterministically on t and input n
        n_t = max(1, n + t)          # string length grows with t
        k_t = max(1, (n_t // 2) + (t % (n_t // 2 + 1)))  # ensure 1 <= k_t <= n_t
        
        # Generate s of length n_t with a deterministic pattern
        # Use 'R', 'G', 'B' in a repeating but shifted pattern
        base = "RGB"
        s_list = []
        for i in range(n_t):
            s_list.append(base[(i + t) % 3])
        s = "".join(s_list)

        # Original algorithm
        p = (k_t + 2) // 2
        l = "RGB" * p
        res = n_t
        for i in range(n_t - k_t + 1):
            c = 0
            for j in range(0, k_t):
                c += (s[i + j] != l[j])
            res = min(res, c)
            c = 0
            for j in range(1, k_t + 1):
                c += (s[i + j - 1] != l[j])
            res = min(res, c)
            c = 0
            for j in range(2, k_t + 2):
                c += (s[i + j - 2] != l[j])
            res = min(res, c)
        results.append(res)

    # For time complexity experiments, we print all results
    for r in results:
        # print(r)
        pass
if __name__ == "__main__":
    # Example call for manual run; adjust n as needed for experiments
    main(10)