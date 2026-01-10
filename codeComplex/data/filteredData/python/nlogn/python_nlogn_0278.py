def main(n):
    # Interpret n as the number of initial pairs; number of update pairs = n as well
    initial_n = n
    update_m = n

    d = {}

    # Deterministic generation of initial pairs
    # a = i, b = i % 5
    for i in range(1, initial_n + 1):
        a = i
        b = i % 5
        d[a] = b

    # Deterministic generation of update pairs
    # a cycles through 1..n, b grows with i to trigger updates
    for i in range(1, update_m + 1):
        a = (i % initial_n) + 1 if initial_n > 0 else 1
        b = i // 2
        if d.get(a) is None:
            d[a] = b
        else:
            if b > d[a]:
                d[a] = b

    ans = 0
    for key in d:
        ans += d[key]

    print(ans)


if __name__ == "__main__":
    main(10)