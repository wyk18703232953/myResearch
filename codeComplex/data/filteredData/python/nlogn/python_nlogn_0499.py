def main(n):
    # Interpret n as the number of (a, b) pairs; derive m deterministically from n.
    if n <= 0:
        return

    # Deterministic construction of a, b
    arr = [i + 1 for i in range(n)]
    brr = [i for i in range(n)]

    # Compute total sums
    sun = sum(arr)
    su = sum(brr)

    # Define m as a deterministic function of n and the sums
    # Here we choose m so that the "interesting" branch (the while loop) is likely executed.
    # m is between su and sun when possible; otherwise clamp.
    mid = (su + sun) // 2
    if su <= mid <= sun:
        m = mid
    elif mid < su:
        m = su
    else:
        m = sun

    dif = [a - b for a, b in zip(arr, brr)]
    ans = 0

    if su > m:
        print(-1)
    elif sun == m:
        print(0)
    else:
        dif.sort()
        j = n - 1
        while sun > m and j >= 0:
            sun -= dif[j]
            ans += 1
            j -= 1
        print(ans)


if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments.
    main(10)