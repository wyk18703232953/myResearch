def main(n):
    # 映射: n -> (n, n)
    m = n
    # 生成确定性数组，长度为 n
    arr = [i % (2 * n + 1) for i in range(1, n + 1)]

    d = {}
    i = 1
    for x in arr:
        if len(d) == m:
            break
        d[x] = i
        i += 1
    if len(d) == m:
        print(min(d.values()), max(d.values()))
    else:
        print(-1, -1)


if __name__ == "__main__":
    main(10)