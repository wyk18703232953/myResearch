def main(n):
    if n <= 0:
        return
    m = max(1, n // 3)
    arr = [i % (2 * m + 1) for i in range(n)]
    s = sum(arr)
    idx = [[] for _ in range(m)]
    for i in range(n):
        idx[arr[i] % m].append(i)
    j = 0
    base = n // m
    for i in range(m):
        while len(idx[i]) > base:
            while True:
                if j < i:
                    j += 1
                elif len(idx[j % m]) >= base:
                    j += 1

                else:
                    break
            last = idx[i].pop()
            arr[last] += (j - i) % m
            idx[j % m].append(last)
    # print(sum(arr) - s)
    pass
    # print(*arr)
    pass
if __name__ == "__main__":
    main(10)