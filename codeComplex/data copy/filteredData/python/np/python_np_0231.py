def main(n):
    # n is the number of elements in the list
    if n < 2:
        print(0)
        return

    # Deterministic parameters based on n
    l = n
    r = 3 * n
    x = max(1, n // 3)

    # Deterministic list of difficulty values
    li = [i + 1 for i in range(n)]

    from itertools import combinations

    z = []
    ans = 0
    for i in range(2, n + 1):
        z += list(combinations(li, i))

    for i in z:
        a = sorted(i)
        if a[-1] - a[0] >= x and r >= sum(a) >= l:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main(10)