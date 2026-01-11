def main(n):
    # Deterministic generation of t
    t = n // 3 + 1

    # Deterministic generation of n segments:
    # hcenter = i * 2, hlen = i % 5 + 1  (ensures non-zero length, simple pattern)
    cont, ans = [], 2
    for i in range(n):
        hcenter = i * 2
        hlen = i % 5 + 1
        cont.append([hcenter - hlen / 2, hcenter + hlen / 2])

    cont.sort(key=lambda item: item[0])

    for i in range(n - 1):
        gap = cont[i + 1][0] - cont[i][1]
        if gap == t:
            ans += 1
        elif gap > t:
            ans += 2

    # print(ans)
    pass
if __name__ == "__main__":
    main(10)