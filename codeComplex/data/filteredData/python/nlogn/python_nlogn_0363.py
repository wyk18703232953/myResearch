from bisect import bisect_right

def main(n):
    # n: length of array a
    if n <= 0:
        print(0)
        return

    # Deterministically generate k and array a based on n
    k = n  # scale k with n for experimentation
    a = [i * 2 + (i % 3) for i in range(n)]  # strictly increasing, deterministic

    a = sorted(a) + [10**9]
    ans = n

    for x in a[:-1]:
        if a[bisect_right(a, x)] <= x + k:
            ans -= 1

    print(ans)


if __name__ == "__main__":
    main(10)