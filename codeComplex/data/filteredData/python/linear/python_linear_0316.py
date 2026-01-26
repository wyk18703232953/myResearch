def main(n):
    # Interpret n as the length of the array; choose a fixed modulus m
    if n <= 0:
        return
    m = max(1, n // 3)  # simple deterministic mapping from n to m
    # Generate a deterministic array of length n
    # Values are constructed to cover various residues modulo m
    arr = [(i * 7 + i // 2) % (2 * m + 5) for i in range(n)]

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
    # print(sum(arr) - s)
    pass
    # print(*arr)
    pass
if __name__ == "__main__":
    # Example: run main with a chosen input scale
    main(10)