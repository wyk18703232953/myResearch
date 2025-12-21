def main(n):
    if n <= 0:
        return 0
    li = [(i % 3) + 1 for i in range(n)]
    dp1 = []
    for i in range(n):
        lis = [-1] * n
        dp1.append(lis)
    dp2 = [0] * n
    for i in range(n):
        dp1[i][i] = li[i]
    for i in range(n):
        dp2[i] = i + 1
    size = 2
    while size <= n:
        i = 0
        while i < n - size + 1:
            j = i + size - 1
            k = i
            while k < j:
                if dp1[i][k] != -1:
                    if dp1[i][k] == dp1[k + 1][j]:
                        dp1[i][j] = dp1[i][k] + 1
                k += 1
            i += 1
        size += 1
    i = 0
    while i < n:
        k = 0
        while k <= i:
            if dp1[k][i] != -1:
                if k == 0:
                    dp2[i] = 1
                else:
                    dp2[i] = min(dp2[i], dp2[k - 1] + 1)
            k += 1
        i += 1
    return dp2[n - 1]

if __name__ == "__main__":
    result = main(5)
    print(result)