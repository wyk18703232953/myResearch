def main(n):
    # Interpret n as both array length and modulus
    if n <= 0:
        return

    m = n

    # Deterministic generation of arr:
    # arr[i] = (i*i + 3*i + 7) % (2*m) ensures variation but is fully deterministic
    arr = [(i * i + 3 * i + 7) % (2 * m) for i in range(n)]

    s = sum(arr)
    x = [[] for _ in range(m)]
    for i in range(n):
        x[arr[i] % m].append(i)

    j = 0
    target = n // m  # this will be 1 when m == n and n > 0
    for i in range(m):
        while len(x[i]) > target:
            while j < i or len(x[j % m]) >= target:
                j += 1
            k = x[i].pop()
            arr[k] += (j - i) % m
            x[j % m].append(k)

    # print(sum(arr) - s)
    pass
    # print(*arr)
    pass
if __name__ == "__main__":
    main(10)