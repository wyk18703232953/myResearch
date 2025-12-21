def main(n):
    N = n
    if N <= 0:
        return 0
    K = max(1, min(N, n // 2 if n >= 2 else 1))
    a = list(range(1, N + 1))
    diff = []
    for i in range(1, N):
        diff.append([i, a[i] - a[i - 1]])
    diff = sorted(diff, key=lambda x: -x[1])
    res = max(a) - min(a)
    k = 0
    while k < K - 1 and k < len(diff):
        res -= diff[k][1]
        k += 1
    return res

if __name__ == "__main__":
    print(main(10))