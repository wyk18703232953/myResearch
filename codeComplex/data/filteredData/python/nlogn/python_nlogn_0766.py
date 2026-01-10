def main(n):
    # Interpret n as both:
    # - number of test cases t = n
    # - size of each array = n
    t = n
    results = []
    for _ in range(t):
        size = n
        # Deterministically generate array a of length size
        # Example pattern: a[i] = (i * 3) % (size + 5) + 1
        a = [(i * 3) % (size + 5) + 1 for i in range(size)]
        a.sort()
        if size >= 2:
            res = min(a[-2] - 1, size - 2)
        else:
            res = 0
        results.append(res)
    # Aggregate output for determinism
    for r in results:
        print(r)


if __name__ == "__main__":
    main(5)