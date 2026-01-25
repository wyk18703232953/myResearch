def main(n):
    # Map n to original parameters:
    # n: length of array a
    # m: modulus parameter, set as max(1, n//3 + 1) to scale with n
    # k: constant cost parameter, set as max(1, n//5 + 1) to scale with n
    if n <= 0:
        print(0)
        return

    m = n // 3 + 1
    k = n // 5 + 1

    # Deterministic generation of a: length n, values depend on index and m,k
    a = [(i * 2 + (i % (m + 1)) + k) for i in range(n)]

    b = [0] * (n + 1)
    for i in range(1, n + 1):
        b[i] = b[i - 1] + m * a[i - 1] - k

    M = [10 ** 20] * m
    ans = 0
    for i in range(0, n + 1):
        idx = i % m
        if b[i] < M[idx]:
            M[idx] = b[i]
        for j in range(0, m):
            if i > j:
                val = b[i] - M[j] - k * ((m * i + m - (i - j)) % m)
                if val > ans:
                    ans = val

    print(ans // m)


if __name__ == "__main__":
    # Example deterministic call; you can change n for experiments
    main(10)