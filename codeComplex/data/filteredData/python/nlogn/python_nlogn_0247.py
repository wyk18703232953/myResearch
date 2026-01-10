def main(n):
    from itertools import accumulate

    def Binary_Search(arr, x, n_):
        l, r = 0, n_ - 1
        while l <= r:
            mid = l + (r - l) // 2
            if arr[mid] == x:
                return mid + 1
            elif arr[mid] > x:
                r = mid - 1
            else:
                l = mid + 1
        return r + 1

    if n <= 0:
        return

    # Define problem size:
    # number of monsters = n
    # number of queries = n
    N = n
    Q = n

    # Deterministic generation of health array a and arrows array b
    # a[i] = (i % 7) + 1  (monster healths, small positive ints)
    # b[i] = (i % 5) + 1  (arrow strengths)
    a = [(i % 7) + 1 for i in range(1, N + 1)]
    b = [(i % 5) + 1 for i in range(1, Q + 1)]

    ps = list(accumulate(a))
    ans = []

    arrows = 0
    for arrow in b:
        arrows += arrow
        if arrows >= ps[-1]:
            ans.append(N)
            arrows = 0
        else:
            res = Binary_Search(ps, arrows, N)
            ans.append(N - res)

    for x in ans:
        print(x)


if __name__ == "__main__":
    main(10)