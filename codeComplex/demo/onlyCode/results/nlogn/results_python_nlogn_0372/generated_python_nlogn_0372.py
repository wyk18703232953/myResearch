def main(n):
    k = n // 2
    arr = [i % (k + 2) for i in range(n)]
    arr.sort()
    f = arr[0]
    p = n
    i = 0
    count = 0
    while i < n:
        while i < n and arr[i] == f:
            i += 1
            count += 1
        if i < n and arr[i] <= f + k:
            p -= count
        if i < n:
            f = arr[i]
            count = 0
        continue
    return p

if __name__ == "__main__":
    print(main(10))