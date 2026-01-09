from collections import Counter

def main(n):
    # Deterministically generate c and array a of length n
    if n <= 0:
        # print(0)
        pass
        return
    c = 1
    a = [(i % 5) + 1 for i in range(n)]

    counter = Counter()
    minus = 0
    count = a.count(c)
    maxi = 0
    for i in range(n):
        if a[i] != c:
            if counter[a[i]] < minus:
                counter[a[i]] = minus
            counter[a[i]] += 1
            maxi = max(maxi, counter[a[i]] + count - minus)

        else:
            minus += 1
    # print(max(maxi, minus))
    pass
if __name__ == "__main__":
    main(10)