def main(n):
    a = [(i % 7) + 1 for i in range(n)]
    a.sort()
    k = 0
    for i in range(n):
        if a[i]:
            k += 1
            for j in range(i + 1, n):
                if a[j] and a[j] % a[i] == 0:
                    a[j] = 0
    # print(k)
    pass
if __name__ == "__main__":
    main(10)