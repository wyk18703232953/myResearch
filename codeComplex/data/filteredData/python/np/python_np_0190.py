from itertools import combinations

def main(n):
    # Interpret n as the length of the array
    # Generate deterministic data based on n, mn, mx, diff derived from n
    length = max(2, n)
    arr = [i % 10 + i // 3 for i in range(1, length + 1)]
    mn = n
    mx = 3 * n
    diff = n // 3

    total = 0
    for i in range(2, length + 1):
        for x in combinations(arr, i):
            s = sum(x)
            if mn <= s <= mx and max(x) - min(x) >= diff:
                total += 1
    print(total)


if __name__ == "__main__":
    main(10)