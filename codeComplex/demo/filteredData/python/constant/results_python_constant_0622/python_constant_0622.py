def main(n):
    cs = n
    results = []
    for c in range(cs):
        # 生成确定性的 (l, r)，确保 l <= r 且规模随 n 增长
        l = 2 * c + 1
        r = l + (c % (n + 1))
        if l % 2 == 0 and r % 2 == 0:
            results.append((r - l) // 2 + l)
        if l % 2 == 1 and r % 2 == 0:
            results.append((r - l + 1) // 2)
        if l % 2 == 0 and r % 2 == 1:
            results.append(-(r - l + 1) // 2)
        if l % 2 == 1 and r % 2 == 1:
            results.append(-(r - l) // 2 - l)
    for x in results:
        # print(x)
        pass
if __name__ == "__main__":
    main(10)