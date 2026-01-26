def Binary_Search(arr, n, x):
    l, r = 0, n - 1
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid + 1
        elif arr[mid] > x:
            r = mid - 1

        else:
            l = mid + 1
    return r + 1


from itertools import accumulate


def main(n):
    if n <= 0:
        return
    q = n
    a = [i + 1 for i in range(n)]
    b = [(i % n) + 1 for i in range(q)]
    ps = list(accumulate(a))
    res = []
    sm = 0
    for i in range(q):
        sm += b[i]
        if sm >= ps[-1]:
            res.append(n)
            sm = 0

        else:
            z = Binary_Search(ps, n, sm)
            res.append(n - z)
    for i in res:
        # print(i)
        pass
if __name__ == "__main__":
    main(10)