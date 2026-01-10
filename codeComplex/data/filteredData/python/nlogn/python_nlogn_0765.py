def main(n):
    # n: number of test cases
    # For each test case i (1-based), define its internal size ni = i + 2
    # Then generate a list l of length ni as l[j] = (j + 1) * (i + 1)
    results = []
    for i in range(1, n + 1):
        ni = i + 2
        l = [(j + 1) * (i + 1) for j in range(ni)]
        l.sort()
        k = max(0, min(ni - 2, l[-2] - 1))
        results.append(k)
    for v in results:
        print(v)


if __name__ == "__main__":
    main(5)