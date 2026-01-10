def main(n):
    # n is the size of the array
    if n <= 0:
        print(0)
        return

    m = n  # unused but kept to mirror original structure

    # Deterministic generation of 'a' based on n
    # Example pattern: a[i] = (i * 3) % (n + 5) + 1, i from 0 to n-1
    a = [(i * 3) % (n + 5) + 1 for i in range(n)]

    h = max(a)
    a.sort()
    a.reverse()
    a.append(0)
    ans = sum(a)
    for i in range(n):
        if a[i + 1] >= a[i]:
            a[i + 1] = a[i] - 1
        ans -= max(a[i] - a[i + 1], 1)
    print(ans)


if __name__ == "__main__":
    main(10)