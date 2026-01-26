from itertools import combinations as cmb

def main(n):
    # n controls the number of elements in array a
    if n < 2:
        print(0)
        return

    # Deterministically generate parameters based on n
    # Ensure l <= r and allow some spread
    l = n
    r = 3 * n
    x = max(1, n // 4)

    # Deterministically generate array a of length n
    # Example: a[i] = i % 10 + i // 2
    a = [(i % 10) + (i // 2) for i in range(1, n + 1)]

    b = []
    a.sort()
    for i in range(2, n + 1):
        b.extend(cmb(a, i))
    ans = 0
    for i in b:
        s = sum(i)
        if s >= l and s <= r:
            if i[-1] - i[0] >= x:
                ans += 1
    print(ans)


if __name__ == "__main__":
    main(10)