def main(n):
    # Deterministically generate input list v of length n
    # Example pattern: v[i] = (i + 1) * (n % 7 + 1)
    v = [(i + 1) * (n % 7 + 1) for i in range(n)]

    n_local = len(v)
    val = 0
    for i in range(n_local):
        a = v[i] // n_local
        arr = v.copy()
        arr[i] = 0
        for j in range(n_local):
            arr[j] += a
        b = v[i] % n_local
        k = i + 1
        l = 0
        while l < b:
            if k > n_local - 1:
                k = 0
            arr[k] += 1
            k += 1
            l += 1

        count = 0
        for j in range(n_local):
            if arr[j] % 2 == 0:
                count += arr[j]
        val = max(val, count)
    # print(val)
    pass
if __name__ == "__main__":
    main(10)