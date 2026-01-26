def main(n):
    from collections import Counter

    ar = [i % 10 for i in range(n)]
    rev = ar[::-1]

    def d(arr, length):
        me = Counter()
        s = 0
        for i in range(length):
            s += i * arr[i]
            s -= me[arr[i]] + me[arr[i] + 1] * arr[i] + me[arr[i] - 1] * arr[i]
            me[arr[i]] += 1
        return s

    result = d(ar, n) - d(rev, n)
    # print(result)
    pass
    return result


if __name__ == "__main__":
    main(10)