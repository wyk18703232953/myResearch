def main(n):
    # Interpret n as the number of problems; generate deterministic parameters and scores
    # n also controls list length and ranges in a deterministic way
    if n <= 0:
        print(0)
        return

    num_problems = n

    # Deterministically derive parameters from n
    # Ensure l <= r and x reasonable relative to values in s
    l = n * 2
    r = n * 4
    x = max(1, n // 3)

    # Generate deterministic scores s of length n
    # Example: s[i] = (i * 2 + 3) % (3*n + 10) + 1 to avoid zeros
    s = [((i * 2 + 3) % (3 * n + 10)) + 1 for i in range(num_problems)]

    olmps = []
    c = []
    v = 0
    for i in range(1 << num_problems):
        olmps.append([])
        for j in range(num_problems):
            if i & (1 << j):
                olmps[-1].append(s[j])
    for o in olmps:
        if l <= sum(o) <= r:
            c.append(o)
    for z in c:
        if max(z) - min(z) >= x:
            v += 1
    print(v)


if __name__ == "__main__":
    main(5)