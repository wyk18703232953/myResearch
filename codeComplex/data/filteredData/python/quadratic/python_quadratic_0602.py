def main(n):
    import copy

    # Deterministic generation of n, m, k, A based on input scale n
    # Ensure m >= 1 and m <= n
    m = max(1, n // 3)
    k = (n // 2) + 1
    A = [((i * 2 + 3) % (n + 5)) - (n // 3) for i in range(n)]

    ANS = 0

    for i in range(m):
        B = copy.deepcopy(A)
        for j in range(i, n, m):
            B[j] -= k

        NOW = 0

        for j in range(i, n):
            if j % m == i:
                NOW = max(NOW + B[j], B[j])

            else:
                NOW += B[j]

            ANS = max(ANS, NOW)

    # print(ANS)
    pass
if __name__ == "__main__":
    main(10)