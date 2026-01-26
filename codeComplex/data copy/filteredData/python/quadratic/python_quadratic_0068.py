def main(n):
    # n controls array length; we also set q = n for scalability
    if n <= 0:
        return

    # deterministic construction of array a
    a = [i * 2 - (i % 3) for i in range(1, n + 1)]

    cnt = 0
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] > a[j]:
                cnt += 1
    even = cnt % 2 == 0

    q = n
    # deterministic construction of q queries
    queries = []
    for i in range(1, q + 1):
        l = (i % n) + 1
        r = ((i * 2) % n) + 1
        if l > r:
            l, r = r, l
        queries.append((l, r))

    for l, r in queries:
        length = r - l + 1
        pairs = length * (length - 1) // 2
        if pairs % 2 == 1:
            even = not even
        if even:
            # print("even")
            pass

        else:
            # print("odd")
            pass
if __name__ == "__main__":
    main(5)