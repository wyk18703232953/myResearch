def main(n):
    # Deterministically generate p and arr based on n
    p = n * 2 + 1  # ensure p > 0
    arr = [(i * 3 + 1) % p for i in range(n)]

    su = 0
    for i in range(n):
        su += arr[i]
    maxi, f = 0, 0
    for i in range(n - 1):
        f += arr[i]
        maxi = max(maxi, f % p + (su - f) % p)
    # print(maxi)
    pass
if __name__ == "__main__":
    main(10)