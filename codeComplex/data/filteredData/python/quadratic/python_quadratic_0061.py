import sys

def main(n):
    # n: length of array, also used to scale number of queries
    if n <= 0:
        return

    # deterministic array of size n
    arr = [((i * 3) % n) for i in range(n)]

    # deterministic number of queries, at least 1
    q = max(1, n)

    inv = 0

    # compute initial inversion parity with same structure
    for i in range(n):
        for j in range(n):
            if i < j and arr[i] > arr[j]:
                inv += 1
            inv = inv % 2

    # deterministic query generation
    for query in range(q):
        # create l, r in 1-based index with l <= r
        l = (query % n) + 1
        r = ((query * 2) % n) + 1
        if l > r:
            l, r = r, l

        diff = r - l
        s = diff // 2
        if diff % 2:
            s += 1

        inv = (inv + (s % 2)) % 2

        if inv:
            # print("odd")
            pass

        else:
            # print("even")
            pass
if __name__ == "__main__":
    main(10)