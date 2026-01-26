import copy

def main(n):
    m = max(1, n // 3)
    k = 2
    A = [(i * 3) % 10 for i in range(n)]

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