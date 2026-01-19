def main(n):
    # Interpret n as the number of elements
    # Deterministic parameters based on n
    l = n  # minimal sum boundary
    r = n * (n + 1) // 2  # maximal possible sum with increasing sequence
    x = max(1, n // 4)  # minimal difference between max and min

    # Deterministic array a of length n
    a = [i + 1 for i in range(n)]

    sumu = 0
    for i in range(2, n + 2):
        for j in combinations(a, i):
            if (r >= sum(j) >= l) and (max(j) - min(j) >= x):
                sumu += 1
    print(sumu)


from itertools import combinations

if __name__ == "__main__":
    main(10)