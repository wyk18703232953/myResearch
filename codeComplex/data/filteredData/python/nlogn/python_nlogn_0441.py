def main(n):
    m = n // 2 + 1
    aa = [((i * 3) % (2 * m + 3)) for i in range(n)]
    if all(x != m for x in aa):
        aa[n // 2] = m

    bb = [-1] * n
    for i in range(n):
        if aa[i] == m:
            bb[i] = 1
        elif aa[i] < m:
            bb[i] = -1

        else:
            bb[i] = 1

    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = bb[i - 1] + prefix_sum[i - 1]

    def mergeSortGoodOrder(arr):
        if len(arr) == 1:
            return arr, 0

        else:
            a = arr[: len(arr) // 2]
            b = arr[len(arr) // 2 :]

            a, ai = mergeSortGoodOrder(a)
            b, bi = mergeSortGoodOrder(b)
            c = []

            i = 0
            j = 0
            good = 0 + ai + bi

            while i < len(a) and j < len(b):
                if a[i] < b[j]:
                    c.append(a[i])
                    i += 1
                    good += len(b) - j

                else:
                    c.append(b[j])
                    j += 1

            c += a[i:]
            c += b[j:]

            return c, good

    idx = 0
    for i in range(n):
        if aa[i] == m:
            idx = i

    _, good = mergeSortGoodOrder(prefix_sum)
    _, bad_left = mergeSortGoodOrder(prefix_sum[: idx + 1])
    _, bad_right = mergeSortGoodOrder(prefix_sum[idx + 1 :])
    first_count = good - bad_left - bad_right

    bb = [-1] * n
    for i in range(n):
        if aa[i] == m + 1:
            bb[i] = 1
        elif aa[i] < m + 1:
            bb[i] = -1

        else:
            bb[i] = 1

    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = bb[i - 1] + prefix_sum[i - 1]

    _, good = mergeSortGoodOrder(prefix_sum)
    _, bad_left = mergeSortGoodOrder(prefix_sum[: idx + 1])
    _, bad_right = mergeSortGoodOrder(prefix_sum[idx + 1 :])
    second_count = good - bad_left - bad_right

    ans = first_count - second_count
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)