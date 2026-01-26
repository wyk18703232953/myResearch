def main(n):
    # n 表示事件数量
    if n <= 0:
        # print(0)
        pass
        return

    # 确定性生成长度数组 l 和类型数组 t
    # l[i] 为正偶数，随 i 有规律变化
    l = [2 * (i % 10 + 1) for i in range(n)]
    # t[i] 在 0,1,2 中循环：0->G,1->W,2->L
    t = [i % 3 for i in range(n)]

    mins = [0 for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        if t[i] != 2:
            mins[i] = max(mins[i + 1] - l[i], 0)

        else:
            mins[i] = mins[i + 1] + l[i]

    curs = ans = st = 0
    for i in range(n):
        if t[i] == 0:
            curs += l[i]
            ans += l[i] * 5
            if curs > mins[i + 1]:
                ol = (curs - mins[i + 1]) // 2
                ol = min(ol, l[i])
                ans -= 4 * ol
                curs -= 2 * ol
        if t[i] == 1:
            st = 1
            curs += l[i]
            ans += l[i] * 3
        if t[i] == 2:
            if curs < l[i]:
                ol = l[i] - curs
                curs = l[i]
                ans += ol * (3 if st else 5)
            curs -= l[i]
            ans += l[i]

    if curs > 0:
        ans -= curs // 2 * 2
    # print(ans // 2)
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 进行规模实验
    main(10)