def main(n):
    # Map n to problem size: use n as the list length, and set k deterministically
    # For determinism and scalability, define k as n // 3
    k = n // 3

    # Generate a deterministic list of integers of length n
    # Pattern: l[i] = (i // 2) % (k + 1) to create duplicates and controlled spread
    l = [ (i // 2) % (k + 1 if k + 1 > 0 else 1) for i in range(n) ]

    # Core logic from original program
    l.sort()
    a = 0
    i = 0
    while i < (n - 1):
        j = i + 1
        while j < n and l[j] == l[i]:
            j += 1
        if j == n:
            break

        else:
            if l[j] <= l[i] + k:
                a += (j - i)
        i = j
    # print(n - a)
    pass
if __name__ == "__main__":
    main(10)