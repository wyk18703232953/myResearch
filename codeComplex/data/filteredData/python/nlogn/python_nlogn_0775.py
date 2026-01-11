def main(n):
    # Generate deterministic input of size n
    # Original input: 
    # n
    # a[0..n-1]
    #
    # Here we map n to the length of array a.
    # Deterministic construction: a[i] = (i * 2 + 3) % (n + 7)
    if n <= 0:
        return "NO"
    a = [(i * 2 + 3) % (n + 7) for i in range(n)]

    # Core logic from original program
    p = a.index(max(a))
    b = sorted(a)
    b.pop()
    ok = 1
    i, j = p - 1, p + 1
    while i >= 0 or j < n:
        if i >= 0 and a[i] == b[-1]:
            b.pop()
            i -= 1
        elif j < n and a[j] == b[-1]:
            b.pop()
            j += 1

        else:
            ok = 0
            break
    return 'YES' if ok else 'NO'


if __name__ == "__main__":
    # Example deterministic call for time complexity experiments
    # print(main(10))
    pass