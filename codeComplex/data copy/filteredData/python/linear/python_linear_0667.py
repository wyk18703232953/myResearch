def main(n):
    # n 表示输入规模，这里映射为数组长度
    if n <= 0:
        # print(0)
        pass
        return

    # 生成确定性的整数数组 a，元素为 i % 7 + 1，保证为正数
    a = [(i % 7) + 1 for i in range(n)]

    # 生成确定性的字符串 b，由 'W'、'G'、'L' 周期性构成
    chars = ['W', 'G', 'L']
    b = ''.join(chars[i % 3] for i in range(n))

    sol = 0
    e = 0
    big = 0
    g = 0
    for i in range(n):
        if b[i] == "W":
            big = 1
            sol += 3 * a[i]
            e += a[i]
        if b[i] == "G":
            sol += 5 * a[i]
            e += a[i]
            g += 2 * a[i]
        if b[i] == "L":
            sol += a[i]
            e -= a[i]
            if e < 0:
                if big:
                    sol -= 3 * e

                else:
                    sol -= 5 * e
                e = 0
        g = min(g, e)
    if e:
        sol -= 2 * g
        sol -= (e - g)

    # print(int(sol))
    pass
if __name__ == "__main__":
    main(10)