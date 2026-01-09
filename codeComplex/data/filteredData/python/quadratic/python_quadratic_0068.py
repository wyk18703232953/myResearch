def main(n):
    # n: length of array a
    # Deterministic construction of a and queries
    a = [(i * 2 + 3) % (n + 7) for i in range(n)]

    cnt = 0
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] > a[j]:
                cnt += 1
    even = cnt % 2 == 0

    # Define number of queries as n for scalability
    q = n
    for i in range(q):
        # Deterministic query generation:
        # l and r are 1-based, ensuring 1 <= l <= r <= n
        l = (i % n) + 1
        r = n - (i % n)
        if l > r:
            l, r = r, l
        length = r - l + 1
        pairs = length * (length - 1) // 2
        if pairs % 2 == 1:
            even = not even
        if even:
            # print('even')
            pass

        else:
            # print('odd')
            pass
if __name__ == "__main__":
    main(5)