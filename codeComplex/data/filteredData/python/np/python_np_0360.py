from random import randint

def main(n):
    # Map n to: t test cases, and for each case dimensions (rows, cols)
    # Keep everything deterministic by seeding the RNG based on n.
    if n <= 0:
        return

    randint.seed(n)
    t = max(1, n // 5)
    results = []

    for case in range(t):
        rows = max(1, n)
        cols = max(1, n // 2)

        # Deterministically construct A based on n, case, i, j
        A = []
        base = n + case * 7
        for i in range(rows):
            row = []
            for j in range(cols):
                val = (base + i * 31 + j * 17) % (n + 10)
                row.append(val)
            A.append(row)

        ans = 0
        for _ in range(100):
            for j in range(cols):
                x = randint(0, rows - 1)
                if x:
                    B = []
                    for i in range(rows):
                        B.append(A[i][j])
                    B = B[x:] + B[:x]
                    for i in range(rows):
                        A[i][j] = B[i]
            c = 0
            for i in range(rows):
                c += max(A[i])
            ans = max(ans, c)
        results.append(ans)

    for v in results:
        print(v)


if __name__ == "__main__":
    main(10)