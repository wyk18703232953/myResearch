def main(n):
    import sys

    # Deterministically generate data based on n
    # We set:
    # - number of initial pairs: n
    # - number of update queries: m = n
    # Keys are 1..n, updates use keys in 1..(2n) with a deterministic pattern.

    # Build initial map d and initial sum sm
    d = {}
    sm = 0
    for i in range(1, n + 1):
        indx = i
        y = (i * 3) % (n + 7) + 1
        d[indx] = y
        sm += y

    # Number of update operations
    m = n
    # Perform updates
    for i in range(1, m + 1):
        # Deterministic index that sometimes exists in d and sometimes not
        indx = (i * 2 - 1)
        y = (i * 5) % (n + 11) + 2
        if indx in d:
            sm -= d[indx]
            if y > d[indx]:
                sm += y

            else:
                sm += d[indx]

        else:
            sm += y

    # Output the final sum to ensure the computation is performed
    sys.stdout.write(str(sm) + "\n")


if __name__ == "__main__":
    # Example call for time complexity experiments; adjust n as needed.
    main(10**5)