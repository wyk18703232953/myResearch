def main(n):
    N = n
    itvs = []
    for i in range(N):
        x = i * 2
        w = (i % 5) + 1
        itvs.append((x - w, x + w))
    itvs.sort(key=lambda x: x[1])

    ans = 0
    end = -(10**9 + 1)
    for l, r in itvs:
        if end <= l:
            ans += 1
            end = r
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)