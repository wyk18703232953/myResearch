def main(n):
    # Deterministically generate input array A of length n
    # Example pattern: A[i] = (i + 1) * (i // 2 + 1)
    A = [(i + 1) * (i // 2 + 1) for i in range(n)]
    A.sort()
    ans = 1 if n > 0 else 0
    for i in range(1, n):
        ok = False
        for j in range(i):
            if A[i] % A[j] == 0:
                ok = True
        if not ok:
            ans += 1
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)