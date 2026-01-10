def main(n):
    # Deterministically generate input permutation-like array a of size n
    # a[1..n], 1-based; use mapping i -> (2*i) % (n+1), with special handling
    a = [0] * (n + 1)
    for i in range(1, n + 1):
        v = (2 * i) % (n + 1)
        if v == 0 or v > n:
            # Map to self to keep indices in [1, n]
            v = i
        a[i] = v

    ans = 0
    for i in range(1, len(a)):
        if a[i] == -1:
            continue
        j = i
        while a[j] != -1:
            prev = j
            j = a[j]
            a[prev] = -1
        ans += 1

    if ans % 2 == 0:
        print("Petr")
    else:
        print("Um_nik")


if __name__ == "__main__":
    main(10)