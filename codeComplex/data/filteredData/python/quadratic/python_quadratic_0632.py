def main(n):
    # Generate deterministic input array of size n
    # Example: a[i] = i+1 ensures mixed divisibility relationships
    a = [i + 1 for i in range(n)]
    a.sort()
    tot = 0
    d = {}
    for i in range(len(a)):
        if a[i] not in d:
            tot += 1
            for j in range(i + 1, len(a), 1):
                if a[j] % a[i] == 0:
                    d[a[j]] = 1
    # print(tot)
    pass
if __name__ == "__main__":
    main(10)