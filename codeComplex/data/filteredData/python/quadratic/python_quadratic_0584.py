def main(n):
    # Interpret n as both the string length and the pattern length
    # Generate deterministic test data equivalent to T test cases
    # Here we set T = n for scalability
    T = n
    results = []
    for t in range(1, T + 1):
        # For each test case:
        # n_t = n, k_t = 1 + (t % n) to vary k while ensuring 1 <= k <= n
        n_t = n
        k_t = 1 + (t % n) if n > 0 else 0

        # Deterministically generate a string s of length n_t over 'R','G','B'
        # pattern: cycle R, G, B using index
        s = ''.join(['RGB'[i % 3] for i in range(n_t)])

        # Core logic from original program (slightly adapted for generated input)
        ans = 10**9
        if k_t > 0 and n_t >= k_t:
            for i in range(n_t - k_t + 1):
                x_sub = s[i:i + k_t]
                curr = ['R', 'G', 'B']
                for l in range(3):
                    m = 0
                    z = l
                    for ch in x_sub:
                        if ch != curr[z]:
                            m += 1
                        z += 1
                        if z == 3:
                            z = 0
                    if m < ans:
                        ans = m

        else:
            # If k_t is invalid (e.g., n == 0), define ans as 0
            ans = 0

        results.append(ans)

    # Output all results
    for res in results:
        # print(res)
        pass
if __name__ == "__main__":
    main(10)