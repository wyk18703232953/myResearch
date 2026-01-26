def main(n):
    # 生成确定性输入数据：长度为 n 的数组 a
    # 保证至少有 1 个值大于 1，以避免明显的退化情况
    if n <= 0:
        # print("NO")
        pass
        return

    # 构造数组 a：a[i] = (i % 3) + 1，保证有很多 >1 的元素
    a = [(i % 3) + 1 for i in range(n)]

    # 原程序逻辑开始
    lf = [(a[i], i) for i in range(n) if a[i] == 1]
    it = [(a[i], i) for i in range(n) if a[i] > 1]
    it.sort(reverse=True)
    while len(lf) < 2 and it:
        lf.append(it.pop())

    ed = []
    if not lf:
        # 无法构造，因为原逻辑需要至少一个 lf 元素
        # print("NO")
        pass
        return

    _, last = lf.pop()

    for i in range(len(it)):
        cap, u = it[i]
        if i != 0:
            ed.append((it[i - 1][1], u))
            cap -= 1
        while lf and cap > 1:
            _, l = lf.pop()
            ed.append((u, l))
            cap -= 1

    if lf:
        ans = 'NO'

    else:
        ans = 'YES %d' % (len(it) + 1,)
        if it:
            ed.append((it[-1][1], last))
            ans1 = str(len(ed))
            ans2 = '\n'.join('%d %d' % (u + 1, v + 1) for u, v in ed)
            ans = '\n'.join([ans, ans1, ans2])

        else:
            ans = 'NO'
    # print(ans)
    pass
if __name__ == "__main__":
    # 示例：使用 n = 10 作为输入规模
    main(10)