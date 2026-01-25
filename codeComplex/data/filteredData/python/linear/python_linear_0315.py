def main(n):
    # Interpret n as both the number of elements and the modulus
    if n <= 0:
        return
    m = n
    # Deterministically generate array of length n
    # Pattern: arr[i] = (i * 2 + 3) % (2 * n + 1)
    limit = 2 * n + 1
    arr = [(i * 2 + 3) % limit for i in range(n)]

    s = sum(arr)
    x = [[] for _ in range(m)]
    for i in range(n):
        x[arr[i] % m].append(i)
    j = 0
    for i in range(m):
        while len(x[i]) > n // m:
            while j < i or len(x[j % m]) >= n // m:
                j += 1
            k = x[i].pop()
            arr[k] += (j - i) % m
            x[j % m].append(k)
    print(sum(arr) - s)
    print(*arr)


if __name__ == "__main__":
    # Example deterministic call for time-complexity experiments
    main(10)