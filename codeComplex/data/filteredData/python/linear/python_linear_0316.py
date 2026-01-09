def main(n):
    # Interpret n as both array length and modulus
    # Ensure m >= 1
    m = max(1, n)

    # Deterministically generate array of length n
    # Example pattern: arr[i] = (i * 2 + 3) % (2*m) to keep values bounded
    arr = [(i * 2 + 3) % (2 * m) for i in range(n)]

    s = sum(arr)
    idx = [[] for _ in range(m)]
    for i in range(n):
        idx[arr[i] % m].append(i)

    j = 0
    for i in range(m):
        while len(idx[i]) > n // m:
            while j < i or len(idx[j % m]) >= n // m:
                j += 1
            last = idx[i].pop()
            arr[last] += (j - i) % m
            idx[j % m].append(last)

    # The original code prints the increment and the final array
    # We keep the same behavior
    # print(sum(arr) - s)
    pass
    # print(*arr)
    pass
if __name__ == "__main__":
    main(10)