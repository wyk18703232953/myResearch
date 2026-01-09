def main(n):
    # n controls the length and values of A; original logic assumes length 14
    size = 14
    if n <= 0:
        n = 1
    # deterministic construction of A of length 14
    base = n
    A = [((base + i * 3) % 20) for i in range(size)]

    ans = 0
    for i in range(14):
        if A[i] == 0:
            continue
        B = A + A
        B[i + 14] = 0
        q, r = divmod(B[i], 14)
        for j in range(1, 15):
            if j <= r:
                B[i + j] += (q + 1)

            else:
                B[i + j] += q
        temp = 0
        for j in range(i + 1, i + 15):
            if B[j] % 2 == 0:
                temp += B[j]
        ans = max(ans, temp)
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)