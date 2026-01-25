def main(n):
    k = max(1, n // 10)
    B = [1] * (n + 1)
    if n >= 0:
        B[0] = 0
    if n >= 1:
        B[1] = 0
    for i in range(2, n + 1):
        if B[i] == 1:
            m = 2
            while m * i <= n:
                B[m * i] = 0
                m += 1
    C = []
    D = []
    for i in range(len(B)):
        if B[i] != 0:
            D.append(i)
    for i in range(1, len(D)):
        c = D[i] + D[i - 1] + 1
        if c <= n:
            C.append(c)
    x = 0
    for i in range(len(C)):
        if B[C[i]] == 1:
            x += 1
    if x >= k:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main(1000)