def main(n):
    # Map n to input structure:
    # n: number of elements in list c
    # l, r, x: derived deterministically from n
    if n <= 0:
        print(0)
        return

    # Deterministic generation of parameters
    l = n
    r = n * (n + 1) // 2
    x = max(1, n // 4)

    # Deterministic generation of list c with strictly increasing values
    c = [i + 1 for i in range(n)]

    from itertools import combinations
    ways_to_choose = 0
    for length in range(2, n + 1):
        for p in combinations(c, length):
            problemset = sorted(p)
            total = sum(problemset)
            if l <= total <= r and problemset[-1] - problemset[0] >= x:
                ways_to_choose += 1

    print(ways_to_choose)


if __name__ == "__main__":
    main(10)