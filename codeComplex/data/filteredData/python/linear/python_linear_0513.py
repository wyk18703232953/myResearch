def main(n):
    if n <= 0:
        # print(0)
        pass
        return

    # Deterministically generate two binary lists a and b of length n
    a = [i % 2 for i in range(n)]
    b = [(i // 2) % 2 for i in range(n)]

    ans = sum(q != w for q, w in zip(a, b))
    i = 1
    while i < n:
        aii = a[i - 1]
        ai = a[i]
        bii = b[i - 1]
        bi = b[i]
        if aii + ai == 1 and bii + bi == 1 and aii != bii and ai != bi:
            ans -= 1
            i += 1
        i += 1

    # print(ans)
    pass
if __name__ == "__main__":
    main(10)