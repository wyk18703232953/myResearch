def main(n):
    # Deterministically generate k and l based on n
    # k must be non-zero; choose a simple deterministic function
    k = (n % 5) + 1  # k in [1,5]

    # Generate a sorted list l of length n with deterministic gaps
    # l[i] = i * k * 2 ensures gaps are multiples of k*2
    l = [i * k * 2 for i in range(n)]

    o = 2
    for i in range(n):
        if i + 1 == n:
            break

        d = abs(l[i] - l[i + 1]) / k
        if d == 2:
            o += 1
        elif d > 2:
            o += 2

    # print(o)
    pass
if __name__ == "__main__":
    main(10)