def main(n):
    a = [(i + 1) * ((i % 5) + 1) for i in range(n)]
    a.sort()
    k = 0
    used = [0] * n
    for i in range(n):
        if used[i]:
            continue
        k += 1
        for j in range(i, n):
            if a[j] % a[i] == 0:
                used[j] = True
    # print(k)
    pass
if __name__ == "__main__":
    main(10)