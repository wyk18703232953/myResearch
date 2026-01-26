def main(n):
    # Ensure n is at least 1 to have a valid array and a pivot m
    if n < 1:
        # print(0)
        pass
        return

    # Deterministic generation of n and m:
    # Original program reads "n m" then an array a of length n containing at least one m.
    # Here: length of a is n, and we set m = n // 2 deterministically.
    m = n // 2

    # Construct a deterministically generated array a of length n
    # Ensure that m appears at least once so that a.index(m) is valid.
    # Pattern: a[i] = (i % (2*m+1)) if m > 0 else 0
    # Then forcibly set a[n//2] = m to guarantee presence.
    if m > 0:
        a = [(i % (2 * m + 1)) for i in range(n)]

    else:
        a = [0] * n
    a[n // 2] = m

    diff = [0] * n
    for i in range(n):
        if a[i] < m:
            diff[i] = -1
        if a[i] > m:
            diff[i] = 1

    aim = a.index(m)
    left = {}
    right = {}
    suml = 0
    for i in reversed(range(aim + 1)):
        suml += diff[i]
        if suml not in left:
            left[suml] = 0
        left[suml] += 1

    sumr = 0
    for i in range(aim, n):
        sumr += diff[i]
        if sumr not in right:
            right[sumr] = 0
        right[sumr] += 1

    ans = 0
    for i in left:
        wk1 = -i
        if wk1 in right:
            ans += left[i] * right[wk1]
        wk1 = 1 - i
        if wk1 in right:
            ans += left[i] * right[wk1]

    # print(ans)
    pass
if __name__ == "__main__":
    # Example deterministic call; adjust n for scaling experiments
    main(10)