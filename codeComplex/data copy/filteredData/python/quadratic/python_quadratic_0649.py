def main(n):
    if n <= 0:
        # print(0)
        pass
        return
    l = [i % (n + 5) + 1 for i in range(n)]
    l.sort()
    s = set([l[0]])
    res = 1
    for i in l:
        f = 1
        for j in s:
            if i % j == 0:
                f = 0
                break
        if f:
            s.add(i)
            res += 1
    # print(res)
    pass
if __name__ == "__main__":
    main(10)