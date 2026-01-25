def main(n):
    # Generate deterministic data:
    # For each row i, create a list of integers of length n: [i*n + j for j in range(1, n+1)]
    a = []
    t = None
    for i in range(n):
        row = [i * n + j for j in range(1, n + 1)]
        s = sum(row)
        if i == 0:
            t = s
        a.append(s)
    a.sort(reverse=True)
    print(a.index(t) + 1)


if __name__ == "__main__":
    main(5)