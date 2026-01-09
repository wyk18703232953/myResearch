def main(n):
    # Deterministic data generation based on n
    # Map n to:
    #   a = 0 (fixed, not used in logic)
    #   b = n
    #   d: strictly increasing list of length n, values in [1, n-1] (when n>1)
    a = 0
    b = n

    if n <= 1:
        # Handle small n deterministically
        d = []

    else:
        # Create a strictly increasing sequence inside (0, b)
        # Example: d[i] = i+1 for i in range(n-1), clipped to b-1
        d = [min(i + 1, b - 1) for i in range(n - 1)]

    e = []
    e1 = []
    mx = 0
    current = 0

    for i in range(len(d)):
        if i % 2 == 0:
            e.append(d[i] - current)

        else:
            e1.append(d[i] - current)
        current = d[i]

    if len(d) == 0:
        # When there is no element in d, i is not defined; handle separately
        # Original logic: if last index i is even -> e1 append, else e append
        # For empty d, treat as i == -1 (odd) to choose a deterministic branch
        # Here we choose equivalent to i % 2 != 0 -> e.append
        e.append(b - current)

    else:
        if i % 2 == 0:
            e1.append(b - current)

        else:
            e.append(b - current)

    mx = sum(e)
    su = 0
    su2 = sum(e1)
    for i in range(len(e)):
        su += e[i]
        mx = max(mx, su + su2 - 1)
        try:
            su2 -= e1[i]
        except:
            break

    # print(mx)
    pass
if __name__ == "__main__":
    # Example deterministic call for time-complexity experiments
    main(10)