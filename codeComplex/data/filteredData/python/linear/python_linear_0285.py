def main(n):
    c, r, o, e = 0, 0, [0] * 300000, [0] * 300000

    # 确定性生成 n 个括号串
    for t in range(1, n + 1):
        s = []
        m = (t % 50) + 1  # 每个串的长度，范围 1~50，随 t 确定性变化
        for i in range(m):
            # 简单确定性模式：根据 (t + i) 的奇偶选择括号
            if (t + i) % 3 == 0:
                s.append('(')

            else:
                s.append(')')
        s = ''.join(s)

        l, nn = 0, 0  # nn 代替原代码中局部的 n
        for ch in s:
            if ch == '(':
                l += 1

            else:
                if l != 0:
                    l -= 1

                else:
                    nn += 1
        if l == 0 and nn == 0:
            c += 1
        elif l != 0 and nn != 0:
            pass
        elif l != 0:
            if l < 300000:
                o[l] += 1

        else:
            if nn < 300000:
                e[nn] += 1

    for i in range(300000):
        if e[i] and o[i]:
            r += e[i] * o[i]
    # print(pow(c, 2) + r)
    pass
if __name__ == "__main__":
    main(1000)