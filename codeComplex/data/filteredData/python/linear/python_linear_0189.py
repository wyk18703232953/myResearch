def main(n):
    # Generate deterministic input data of size n
    # Here, we create a list a of length n with deterministic values
    a = [(i % 10) + 1 for i in range(n)]
    s = sum(a)
    new = 0
    i = 0
    # Handle edge case when n == 0 to avoid index error
    while i < n and 2 * (new + a[i]) < s:
        new += a[i]
        i += 1
    # If loop ends because i == n, original logic would not print anything;
    # but here we cap i to n-1 for consistency when printing i+1
    if i == n:
        # print(n)
        pass

    else:
        # print(i + 1)
        pass
if __name__ == "__main__":
    main(10)