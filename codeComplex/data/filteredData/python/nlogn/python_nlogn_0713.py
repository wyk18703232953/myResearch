def main(n):
    ans = ["sjfnb", "cslnb"]
    l = [(i // 2) for i in range(n)]
    l.sort()
    d = set()
    e = 0
    s = 0
    for i in range(n):
        if l[i] in d:
            e += 1
            s = l[i]
        d.add(l[i])
    if e > 1 or l.count(0) > 1 or (s - 1) in d:
        print(ans[1])
    else:
        l = [l[i] - i for i in range(n)]
        print(ans[1 - sum(l) % 2])


if __name__ == "__main__":
    main(10)