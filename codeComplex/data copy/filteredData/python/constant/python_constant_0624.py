def getsum(N):
    A = (N + 1) // 2
    r1 = -A + A * (A + 1)
    B = N // 2
    r2 = B * (B + 1)
    return -r1 + r2

def main(n):
    Q = n
    total = 0
    for i in range(1, Q + 1):
        L = i
        R = 2 * i
        total += getsum(R) - getsum(L - 1)
    # print(total)
    pass
if __name__ == "__main__":
    main(10)