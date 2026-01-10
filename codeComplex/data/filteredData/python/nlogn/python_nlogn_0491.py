def main(n):
    m = 5 * n
    ans = 0
    temp = [0 for _ in range(n)]
    pairs = []
    for i in range(n):
        l = i + 1
        r = i // 2 + 1
        pairs.append((l, r))
    for i in range(n):
        l, r = pairs[i]
        ans += l
        temp[i] = l - r
    temp.sort(reverse=True)
    if ans <= m:
        print(0)
    else:
        for i in range(n):
            ans -= temp[i]
            if ans <= m:
                print(i + 1)
                break
        else:
            print(-1)


if __name__ == "__main__":
    main(10)