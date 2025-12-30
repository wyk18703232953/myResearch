import random

def main(n):
    # 生成规模为 n 的测试数据：a[i] 为 1~n 之间的随机整数
    a = [random.randint(1, n) for _ in range(n)]

    lf = [(a[i], i) for i in range(n) if a[i] == 1]
    it = [(a[i], i) for i in range(n) if a[i] > 1]
    it.sort(reverse=True)

    while len(lf) < 2 and it:
        lf.append(it.pop())

    # 若 it 不足以补到两个 lf，则构造不出原逻辑的结构
    if len(lf) < 2:
        print("NO")
        return

    ed = []
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
        ed.append((it[-1][1], last))
        ans1 = str(len(ed))
        ans2 = '\n'.join('%d %d' % (u + 1, v + 1) for u, v in ed)
        ans = '\n'.join([ans, ans1, ans2])
    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)