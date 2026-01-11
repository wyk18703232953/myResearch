def main(n):
    # Interpret n as: length of array = n, and k = max(1, n//3)
    if n <= 0:
        return
    k = max(1, n // 3)
    # Deterministic array generation
    # Example: arr[i] = (i * 2 + 3) % (n + 7) + 1
    arr = [((i * 2 + 3) % (n + 7)) + 1 for i in range(n)]

    bs = [[x, i + 1] for i, x in enumerate(arr)]
    bs.sort(reverse=True)
    k = min(k, n)
    cs = [bs[i][1] for i in range(k)]
    ans = sum(bs[i][0] for i in range(k))
    cs.sort()
    # print(ans)
    pass

    if k == 1:
        # print(n)
        pass

    else:
        # print(cs[0], end=" ")
        pass
        for i in range(1, k - 1):
            # print(cs[i] - cs[i - 1], end=" ")
            pass
        # print(n - cs[k - 2])
        pass
if __name__ == "__main__":
    main(10)