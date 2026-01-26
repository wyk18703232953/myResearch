def main(n):
    # Deterministic generation of k and arr based on n
    # k is the range of possible values in arr, at least 1
    k = max(1, n // 3)
    # Generate arr of length n with values cycling from 1 to k
    arr = [(i % k) + 1 for i in range(n)]

    d = {}
    for i in arr:
        if i in d:
            d[i] += 1

        else:
            d[i] = 1
    flag = True
    for i in range(100, 0, -1):
        t2 = 0
        for j in d.values():
            t2 += j // i
        if t2 >= n:
            # print(i)
            pass
            flag = False
            break
    if flag:
        # print(0)
        pass
if __name__ == "__main__":
    main(10)