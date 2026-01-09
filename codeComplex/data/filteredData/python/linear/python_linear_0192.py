def main(n):
    A = n + 1
    B = n // 2 + 1
    C = max(1, n // 3)
    T = n + 5
    a = [(i * 2) % T for i in range(n)]
    ans = 0
    for i in range(n):
        su, cur = A, A
        for j in range(a[i], T):
            cur -= B
            su = max(su, (j - a[i] + 1) * C + cur)
        ans += su
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)