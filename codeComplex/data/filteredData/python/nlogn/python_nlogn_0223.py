def main(n):
    # Interpret n as the size of array a
    # We also need m; choose a deterministic function of n
    m = n // 2 + 1

    # Deterministically generate input array 'a' of length n
    # Example: a decreasing sequence to mimic reversed input reading
    # Original code: a = rints()[::-1]
    # Here we create base array b as increasing, then reverse to get decreasing a
    b = [i + 1 for i in range(n)]
    a = b[::-1]

    cur, ans = 2, -1

    # Handle small n cases safely
    if n < 2:
        print(-1)
        return

    for i in range(n - 2):
        cur = max(cur, i + 2)
        for j in range(cur, n):
            if a[i] - a[j] < 1:
                cur += 1
                continue

            if a[i] - a[j] > m:
                break

            cur += 1
            v = (a[i] - a[j - 1]) / (a[i] - a[j])
            ans = max(ans, v)

    print(ans)


if __name__ == "__main__":
    # Example call for scalability experiments
    main(1000)