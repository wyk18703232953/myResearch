def main(n):
    # n: length of array a
    a = [(i * 2 + 3) % (n + 5) for i in range(n)]

    cnt = 0
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] > a[j]:
                cnt += 1
    even = cnt % 2 == 0

    # Define number of queries as n (scalable with n)
    q = n
    ans = []
    for i in range(q):
        # Deterministically generate l, r based on i and n
        l = i % n
        r = (n - 1 - i) % n
        if l > r:
            l, r = r, l
        l += 1
        r += 1

        length = r - l + 1
        pairs = length * (length - 1) // 2
        if pairs % 2 == 1:
            even = not even
        if even:
            ans.append('even')

        else:
            ans.append('odd')
    # print('\n'.join(ans))
    pass
if __name__ == "__main__":
    main(5)