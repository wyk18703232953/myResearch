def main(n):
    # Generate deterministic input array a of size n
    # Example: a[i] = (i * 2) % (n + 3)
    a = [(i * 2) % (n + 3) for i in range(n)]
    a = sorted(a)

    ans = [0] * n
    if n > 0:
        ans[0] = 1
        f = ans[0] != a[0]
        for i in range(1, n):
            ans[i] = a[i - 1]
            if ans[i] != a[i]:
                f = True

        m = 10 ** 9
        if not f:
            for i in range(n - 1, -1, -1):
                if ans[i] < m:
                    ans[i] += 1
                    break

    print(' '.join(map(str, ans)))


if __name__ == "__main__":
    main(10)