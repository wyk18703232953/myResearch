def main(n):
    # Map n to array length; ensure at least 1 element
    length = max(1, n)

    # Deterministic generation of k based on n
    # Keep k reasonably large and varying with n
    k = max(1, (n * 17) % 10**9 + 7)

    # Deterministic generation of array a of length `length`
    # Values are constructed arithmetically from index and k
    a = [i * 1234567 + (k % (i + 1)) for i in range(length)]

    # Core logic from original program
    bank = {}

    # Preparation
    for i in range(length):
        arg = (len(str(a[i])), a[i] % k)
        bank[arg] = bank.get(arg, 0) + 1

    ans = 0
    # Query
    for i in range(length):
        ten = 1
        for j in range(1, 11):
            ten *= 10
            frontMod = (a[i] * ten) % k
            req = (k - frontMod) % k
            got = bank.get((j, req), 0)
            ans += got

    # Deal with Same Index
    for i in range(length):
        cur = str(a[i])
        cur = cur * 2
        tst = int(cur)
        if tst % k == 0:
            ans -= 1

    # print(ans)
    pass
if __name__ == "__main__":
    main(10)