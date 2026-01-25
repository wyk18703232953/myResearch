from math import ceil

def brute(n, m, k, A):
    ans = 0
    val = (0, 0)
    for i in range(n):
        for j in range(i, n):
            cur = sum(A[i:j+1]) - k * (ceil((j - i + 1) / m))
            if ans < cur:
                ans = cur
                val = (i, j)
    return val, ans

def main(n):
    if n <= 0:
        print(0)
        return

    m = max(1, n // 3)
    k = n // 2

    A = [((i * 2) - (n // 2)) for i in range(n)]

    bestbest = 0

    for off in range(m):
        B = A[off:]
        C = []
        canstart = []
        for i in range(len(B)):
            if i % m == 0:
                C.append(-k)
                canstart.append(1)
            canstart.append(0)
            C.append(B[i])

        best = 0
        run = 0

        for i in range(len(C)):
            run += C[i]
            if run < -k:
                run = -k
            best = max(best, run)
        bestbest = max(bestbest, best)

    print(bestbest)

if __name__ == "__main__":
    main(1000)