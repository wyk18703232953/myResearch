import math

def main(n):
    # Interpret n as the size of the initial array and set q proportional to n
    if n < 2:
        n = 2
    q = n

    # Deterministically generate arr of length n: [1, 2, ..., n] with a simple pattern
    # To ensure interesting behavior, make the maximum not at the ends
    arr = [(i * 2 + 3) % (3 * n + 7) for i in range(n)]
    # Guarantee at least one maximum in the middle for consistent behavior
    if n >= 3:
        arr[n // 2] = max(arr) + 5

    # Original logic starts here
    orig_n = n
    for _ in range(orig_n):
        arr.append(0)
    maxx = 0  # kept to preserve structure, though unused

    ind = arr.index(max(arr))
    ans = []
    ptr1 = 0
    ptr2 = orig_n
    for _ in range(ind):
        ans.append([arr[ptr1], arr[ptr1 + 1]])
        if arr[ptr1] > arr[ptr1 + 1]:
            arr[ptr2] = arr[ptr1 + 1]
            arr[ptr1 + 1] = arr[ptr1]

        else:
            arr[ptr2] = arr[ptr1]
        ptr1 += 1
        ptr2 += 1

    # Deterministically generate q queries; cover small and large m
    queries = []
    for i in range(q):
        if i < ind:
            m = i + 1

        else:
            m = ind + 1 + (i - ind) % (orig_n * 2 + 1)
        queries.append(m)

    for m in queries:
        if m <= ind:
            # print(*ans[m - 1])
            pass

        else:
            mm = m - ind
            mm = mm % (orig_n - 1)
            if mm == 0:
                mm += orig_n - 1
            # print(arr[ind], arr[ind + mm])
            pass
if __name__ == "__main__":
    main(10)