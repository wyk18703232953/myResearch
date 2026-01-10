def main(n):
    # n controls the number of pairs in each dictionary
    dicta = {}
    dictb = {}

    # Generate first set of key-value pairs deterministically
    # Keys: 0..n-1, Values: i % 7 + i // 3 (arbitrary deterministic function)
    for i in range(n):
        a = i
        x = (i % 7) + (i // 3)
        dicta[a] = x

    # Generate second set of key-value pairs deterministically
    # Keys: i+1 to create overlap and non-overlap, Values: i % 5 + i // 2
    m = n
    for i in range(m):
        b = i + 1
        y = (i % 5) + (i // 2)
        dictb[b] = y

    ans = 0
    # Core logic preserved
    for i in list(dicta.keys()):
        if i in dictb:
            ans += max(dicta[i], dictb[i])
            del dictb[i]
        else:
            ans += dicta[i]
    for v in dictb.values():
        ans += v

    print(ans)


if __name__ == "__main__":
    main(10)