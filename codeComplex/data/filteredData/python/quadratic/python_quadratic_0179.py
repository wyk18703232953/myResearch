def main(n):
    # 映射：n -> 输入规模
    # 这里令 k = max(1, n // 2)，p 为长度为 n 的确定性整数序列
    if n <= 0:
        return
    k = max(1, n // 2)

    # 确定性构造 p：略微变化的数列，保证有重复和间隔
    # p[i] = (i * 3) % (2 * n) 保证范围可控且与 n 相关
    p = [(i * 3) % (2 * n) for i in range(n)]

    processed = set()
    color = {}
    length = {}
    ans = []

    def exists(p_local, elt, d):
        for e in p_local:
            if e > elt:
                if e <= elt + d:
                    return True
                elif e - d <= elt + d:
                    return False
        return False

    def exists2(p_local, elt, d):
        for e in p_local:
            if e > elt:
                if e <= elt + d:
                    return False
                elif e - d <= elt + d:
                    return [True, e - d]
        return False

    for i in range(n):
        elt = p[i]
        if elt in processed:
            ans.append(color[elt])

        else:
            processed.add(elt)
            new = 1
            run = True
            for j in range(1, k):
                if elt - j < 0:
                    break
                elif (elt - j) not in processed:
                    processed.add(elt - j)
                    new += 1
                elif length[elt - j] + new <= k:
                    for i2 in range(length[elt - j] + new):
                        color[elt - i2] = color[elt - j]
                    length[elt] = length[elt - j] + new
                    run = False
                    break

                else:
                    break
            if run:
                for j in range(new):
                    color[elt - j] = elt - new + 1
                length[elt] = new

    s = str(color[p[0]])
    for elt in p[1:]:
        s += ' ' + str(color[elt])
    # print(s)
    pass
if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    main(10)