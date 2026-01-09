def main(n):
    m = n
    A = [i % n + 1 for i in range(m)]
    L = [0] * n
    for i in range(m):
        L[A[i] - 1] += 1
    # print(min(L))
    pass
if __name__ == "__main__":
    main(10)