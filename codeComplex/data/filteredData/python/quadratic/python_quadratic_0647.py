def main(n):
    # Deterministically generate input array of size n
    # Example pattern: a[i] = i + 1
    a = [i + 1 for i in range(n)]

    a.sort()
    ans = 0
    while a:
        m = a[0]
        b = []
        for x in a[1:]:
            if x % m != 0:
                b.append(x)
        a = b
        ans += 1
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)