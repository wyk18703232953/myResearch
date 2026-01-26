def main(n):
    if n <= 0:
        # print(0)
        pass
        return
    a = [(i * 2 + 1) for i in range(n)]
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