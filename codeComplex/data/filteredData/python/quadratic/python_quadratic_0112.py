def main(n):
    # 使用 n 生成确定性的 n×n 字符矩阵 a 和 b
    # a[i][j] = chr(ord('a') + (i + j) % 26)
    # b 为在 a 的基础上做一次旋转后（或者不旋转）得到的矩阵，用于保持逻辑一致
    a = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(chr(ord('a') + (i + j) % 26))
        a.append(''.join(row))

    # 生成目标矩阵 b：这里固定做一次 r 变换，保持可重复且确定
    # 若希望有时匹配有时不匹配，可以根据 n 的奇偶决定是否旋转
    def r_gen(d):
        c = []
        for i in range(n):
            temp = ""
            for j in range(n):
                temp += d[j][n - i - 1]
            c.append(temp)
        return c

    if n % 2 == 0:
        b = r_gen(a)
    else:
        b = a[:]  # 直接等于 a，使得一定能匹配

    def h(d):
        c = []
        for i in range(n):
            c.append(d[n - i - 1])
        return c

    def r(d):
        c = []
        for i in range(n):
            temp = ""
            for j in range(n):
                temp += d[j][n - i - 1]
            c.append(temp)
        return c

    yes = 0
    a_cur = a
    for _ in range(4):
        if a_cur == b:
            print('YES')
            yes = 1
            break
        a_cur = r(a_cur)
    if yes == 0:
        a_cur = h(a_cur)
        for _ in range(4):
            if a_cur == b:
                print('YES')
                yes = 1
                break
            a_cur = r(a_cur)
    if yes == 0:
        print('NO')


if __name__ == "__main__":
    main(5)