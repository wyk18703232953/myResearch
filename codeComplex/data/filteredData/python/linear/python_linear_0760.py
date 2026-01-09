def main(n):
    a = [(i * 2 - 3) for i in range(n)]

    for i in range(n):
        if a[i] >= 0:
            a[i] = -a[i] - 1

    if n % 2:
        m = min(a)
        for i in range(n):
            if a[i] == m:
                a[i] = -a[i] - 1
                break

    # print(*a)
    pass
if __name__ == "__main__":
    main(10)