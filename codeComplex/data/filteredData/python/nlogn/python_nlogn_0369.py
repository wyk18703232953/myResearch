def main(n):
    k = n // 2
    a = [(i * 3) % (2 * n + 1) for i in range(n)]
    j = 0
    a.sort()
    n1 = n
    for i in range(n):
        while j < n and a[j] < a[i]:
            if a[i] <= a[j] + k:
                n1 -= 1
            j += 1
    print(n1)


if __name__ == "__main__":
    main(10)