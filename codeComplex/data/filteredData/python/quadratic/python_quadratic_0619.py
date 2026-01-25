from math import *

def main(n):
    # n 作为数组长度规模；m 和 k 由 n 确定性生成
    if n <= 0:
        print(0)
        return
    m = max(1, n // 3)
    k = n // 2

    l = [i % 7 - 3 for i in range(1, n + 1)]

    a = [0 for _ in range(n + 1)]
    ans = 0
    for M in range(m):
        min1 = 0
        for i in range(1, n + 1):
            a[i] = a[i - 1] + l[i - 1]
            if (i % m == M):
                a[i] -= k
                ans = max(ans, a[i] - min1)
            min1 = min(min1, a[i])
    print(ans)

if __name__ == "__main__":
    main(10)