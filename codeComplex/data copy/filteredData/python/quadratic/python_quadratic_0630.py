def main(n):
    # Generate deterministic test data of size n for problem A.
    # Input structure of original A():
    #   n
    #   a_1 a_2 ... a_n
    #
    # Here we map the parameter n to the list length.
    # Construct a[i] = (i+1)*(i%3 + 1) to have some repetition and divisibility structure.
    if n <= 0:
        # print(0)
        pass
        return
    a = [(i + 1) * ((i % 3) + 1) for i in range(n)]

    # Core logic from original A(), with input removed.
    a.sort()
    f = [1] * n
    p = 0
    ans = 0
    while p < n:
        while p < n and not f[p]:
            p += 1
        if p == n:
            break
        ans += 1
        for i in range(n):
            if a[i] % a[p] == 0:
                f[i] = 0
    # print(ans)
    pass
if __name__ == "__main__":
    # Example deterministic call; adjust n for different input scales
    main(10)