def main(n):
    # Interpret n as the upper bound 'a'
    a = max(2, n)
    # Derive k deterministically from a, keep it within a reasonable range
    k = max(1, a // 10)

    # Generate primes up to a
    p = []
    for x in range(2, a + 1):
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                break
        else:
            p.append(x)

    # Count primes of the form p[i] + p[i+1] + 1 that are <= a
    c = 0
    for i in range(0, len(p) - 1):
        s = p[i] + p[i + 1] + 1
        for j in range(2, int(s ** 0.5) + 1):
            if s % j == 0:
                break
        else:
            if s <= a:
                c += 1

    if c >= k:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    # Example deterministic call for time-complexity experiments
    main(1000)