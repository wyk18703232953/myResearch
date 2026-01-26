def main(n):
    # n: length of array arr
    if n <= 0:
        # print(0)
        pass
        return

    # Deterministically generate k and arr based on n
    # Make k reasonably sized but dependent on n
    k = max(1, n // 2 + 3)

    # Generate arr as deterministic sequence of positive integers
    # Example: a[i] = (i * 7 + 3) % (10**9 + 7)
    MOD = 10**9 + 7
    arr = [(i * 7 + 3) % MOD for i in range(1, n + 1)]

    d = [{} for _ in range(11)]
    for i in range(n):
        st = arr[i]
        for j in range(11):
            r = st % k
            try:
                d[j][r] += 1
            except KeyError:
                d[j][r] = 1
            st *= 10

    count_pair = 0
    for i in arr:
        st = str(i)
        l = len(st)
        mod_st = (k - (i % k)) % k
        if mod_st in d[l]:
            count_pair += d[l][mod_st]
            if int(st + st) % k == 0:
                count_pair -= 1

    # print(count_pair)
    pass
if __name__ == "__main__":
    main(10)