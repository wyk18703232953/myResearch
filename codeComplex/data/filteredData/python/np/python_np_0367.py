from random import randint

def run_single_case(n, m, A):
    ans = 0
    for _ in range(100):
        for j in range(m):
            x = randint(0, n - 1)
            if x:
                B = []
                for i in range(n):
                    B.append(A[i][j])
                B = B[x:] + B[:x]
                for i in range(n):
                    A[i][j] = B[i]
        c = 0
        for i in range(n):
            c += max(A[i])
        ans = max(ans, c)
    return ans

def main(n):
    t = n
    res = []
    for case_id in range(1, t + 1):
        rows = max(1, case_id)
        cols = max(1, n)
        A = [[(i * cols + j + case_id) % (rows * cols + 7) for j in range(cols)] for i in range(rows)]
        ans = run_single_case(rows, cols, [row[:] for row in A])
        res.append(ans)
    for v in res:
        print(v)

if __name__ == "__main__":
    main(5)