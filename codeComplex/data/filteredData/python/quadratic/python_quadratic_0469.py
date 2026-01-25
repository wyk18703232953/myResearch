def main(n):
    # 输入结构：一个整数 n，两个长度为 n 的整数列表 l, r
    # 由 n 确定性生成 l, r
    l = [i % 3 for i in range(n)]
    r = [(n - 1 - i) % 4 for i in range(n)]

    mp = {i: i for i in range(n)}
    out = [-1] * n
    v = 0

    a = n
    done = set()
    while v < n:
        ids = set()
        for j in range(n):
            if l[j] == 0 and r[j] == 0 and j not in done:
                ids.add(j)
                done.add(j)
        if len(ids) == 0:
            print('NO')
            return
        v += len(ids)
        for i in ids:
            out[mp[i]] = a
            for j in range(len(l)):
                if j < i:
                    r[j] -= 1
                else:
                    l[j] -= 1
        a -= 1
    print('YES')
    print(' '.join(map(str, out)))


if __name__ == "__main__":
    # 示例调用，可按需要修改 n 以做时间复杂度实验
    main(5)