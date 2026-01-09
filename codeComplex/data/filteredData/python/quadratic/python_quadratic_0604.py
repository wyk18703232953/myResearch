from math import ceil

def brute(n, m, k, A):
    ans = 0
    val = (0, 0)
    for i in range(n):
        for j in range(i, n):
            current = sum(A[i:j+1]) - k * (ceil((j - i + 1) / m))
            if ans < current:
                ans = current
                val = (i, j)
    return val, ans

def main(n):
    m = max(1, n // 3)
    k = max(1, n // 5)
    A = [((i * 7) % 10) - 5 for i in range(n)]

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

    # print(bestbest)
    pass
if __name__ == "__main__":
    main(1000)