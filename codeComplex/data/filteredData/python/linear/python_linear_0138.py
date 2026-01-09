def main(n):
    # Deterministically generate input array a of length n
    # Example: a[i] = (i * 2) % (n + 3)
    a = [(i * 2) % (n + 3) for i in range(n)]

    b = []
    maxi = 0
    for i in range(n):
        maxi = max(maxi, a[i] + 1)
        b.append(maxi)

    c = []
    count = b[-1] if n > 0 else 0
    for i in range(n - 1, -1, -1):
        if count - 1 >= b[i]:
            count -= 1
            c.append(count)

        else:
            c.append(count)
    c = c[::-1]

    ans = 0
    for i in range(n):
        ans += (c[i] - a[i] - 1)

    # print(ans)
    pass
if __name__ == "__main__":
    main(10)