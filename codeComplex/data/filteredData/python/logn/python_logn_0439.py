def main(n):
    # Interpret n as the number of test cases
    test = n
    results = []
    while test:
        test -= 1

        # Deterministic generation of (n_val, k_val) for each test case
        n_val = 2 + test % 40
        k_val = 1 + (test * 3) % (4 * (n_val + 1))

        n_local = n_val
        k_local = k_val

        if n_local == 2 and k_local == 3:
            results.append("NO")
            continue
        if n_local >= 32:
            results.append(f"YES {n_local - 1}")
            continue
        val = [0]
        for i in range(1, n_local + 1):
            val.append(4 * val[i - 1] + 1)
        if val[n_local] < k_local:
            results.append("NO")
            continue
        s = 0
        t = 2
        rem = 0
        flag = 0
        while s + t - 1 <= k_local and n_local > 0:
            s = s + t - 1
            t *= 2
            n_local -= 1
        results.append(f"YES {n_local}")

    for line in results:
        # print(line)
        pass
if __name__ == "__main__":
    main(10)