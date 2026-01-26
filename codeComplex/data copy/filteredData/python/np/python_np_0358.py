def main(n):
    # Interpret n as both number of rows and columns
    rows = n
    cols = n

    # Deterministic generation of t test cases
    # For simplicity and scalability experiment, use t = 1
    t = 1

    for testcases in range(t):
        # Generate A as rows x cols matrix deterministically
        # Example: A[i][j] = (i * cols + j) % (n + 7)
        A = [[(i * cols + j) % (n + 7) for j in range(cols)] for i in range(rows)]

        m = cols

        B = []
        for j in range(m):
            B.append([A[i][j] for i in range(rows)])

        B.sort(key=lambda x: max(x), reverse=True)

        B = B[:rows]

        LEN = len(B)

        if LEN == 1:
            print(sum(B[0]))

        elif LEN == 2:
            ANS = 0
            for i in range(rows):
                tmp = 0
                for k in range(rows):
                    tmp += max(B[0][k], B[1][(i + k) % rows])
                ANS = max(ANS, tmp)
            print(ANS)

        elif LEN == 3:
            ANS = 0
            for i in range(rows):
                for j in range(rows):
                    tmp = 0
                    for k in range(rows):
                        tmp += max(
                            B[0][k],
                            B[1][(i + k) % rows],
                            B[2][(j + k) % rows],
                        )
                    ANS = max(ANS, tmp)
            print(ANS)

        elif LEN == 4:
            ANS = 0
            for i in range(rows):
                for j in range(rows):
                    for l in range(rows):
                        tmp = 0
                        for k in range(rows):
                            tmp += max(
                                B[0][k],
                                B[1][(i + k) % rows],
                                B[2][(j + k) % rows],
                                B[3][(l + k) % rows],
                            )
                        ANS = max(ANS, tmp)
            print(ANS)


if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(5)