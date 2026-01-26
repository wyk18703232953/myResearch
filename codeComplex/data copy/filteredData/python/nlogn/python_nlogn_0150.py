def main(n):
    # Deterministically generate inputs based on n
    # Interpret n as the length of array a
    # Define k as a simple deterministic function of n
    if n <= 0:
        return

    k = (n % 5) + 2  # k in [2,6], avoid k=1 special trivial case as default
    original_n = n

    # Generate a list 'a' of length n deterministically
    # Example: a[i] = i + 1
    a = [i + 1 for i in range(n)]

    # Core logic from original program
    if k == 1:
        # print(original_n)
        pass
        return

    a.sort()
    c = dict(zip(a, range(n)))
    a = c
    b = {}
    count = {}

    for x in a:
        if x % k == 0 and int(x / k) in a:
            b[x] = b[int(x / k)]
            count[b[int(x / k)]] += 1

        else:
            b[x] = x
            count[x] = 1

    result = original_n
    for _, y in count.items():
        result -= int(y / 2)

    # print(result)
    pass
if __name__ == "__main__":
    main(10)