from math import ceil
import random

def brute(n, m, k, A):
    best_sum = float('-inf')
    best_interval = (0, 0)
    for i in range(n):
        s = 0
        for j in range(i, n):
            s += A[j]
            val = s - k * ceil((j - i + 1) / m)
            if val > best_sum:
                best_sum = val
                best_interval = (i, j)
    return best_interval, best_sum

def solve(n, m, k, A):
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
        for x in C:
            run += x
            if run < -k:
                run = -k
            if run > best:
                best = run
        if best > bestbest:
            bestbest = best
    return bestbest

def generate_test_data(n):
    # 简单生成：m 和 k 与 n 同量级，A 为 [-10,10] 之间的随机整数
    if n <= 0:
        return 0, 0, 0, []
    m = random.randint(1, n)
    k = random.randint(1, max(1, n // 2))
    A = [random.randint(-10, 10) for _ in range(n)]
    return n, m, k, A

def main(n):
    n, m, k, A = generate_test_data(n)
    # 如果需要，可调用 brute 做校验：
    # interval, brute_ans = brute(n, m, k, A)
    ans = solve(n, m, k, A)
    print(ans)

if __name__ == "__main__":
    # 示例：用 n=10 运行一次
    main(10)