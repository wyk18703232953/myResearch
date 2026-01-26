def main(n):
    # Generate deterministic test data of size n
    # Each element is a pair (k, m)
    # Example: k grows roughly linearly, m is a small deterministic function of index
    l = []
    for i in range(n):
        k = i * 3 + 1
        m = (i * 2 + 1) % (n // 2 + 1) if n > 1 else 1
        l.append((k, m))

    l.sort(key=lambda x: x[0] + x[1])

    if n == 0:
        ans = 0

    else:
        last = 0
        ans = 1

        for i in range(1, n):
            if l[i][0] - l[i][1] >= l[last][0] - l[last][1] and abs(l[i][0] - l[last][0]) >= l[i][1] + l[last][1]:
                last = i
                ans = ans + 1

    # print(ans)
    pass
if __name__ == "__main__":
    main(1000)