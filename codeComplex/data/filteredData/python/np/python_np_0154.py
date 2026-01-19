from itertools import combinations

def main(n):
    # Deterministic generation of parameters based on n
    # Ensure basic valid ranges
    l = n
    r = 3 * n
    x = max(1, n // 5)

    # Generate array of size n deterministically
    arr = [(i * 2 + 3) % (3 * n + 7) + 1 for i in range(n)]

    ans = 0
    for i in range(2, n + 1):
        brr = combinations(arr, i)
        for j in brr:
            s = sum(j)
            if l <= s <= r and max(j) - min(j) >= x:
                ans += 1
    print(ans)

if __name__ == "__main__":
    main(10)