def main(n):
    # 确定性生成长度为 n 的字符串 t
    # 使用小写字母循环构造，例如 n=1 -> "a", n=2 -> "ab", ..., n=27 -> "abcdefghijklmnopqrstuvwxyz" + "a"
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    if n <= 0:
        t = ""

    else:
        t = "".join(alphabet[i % 26] for i in range(n))

    n = len(t)
    maxi = 0

    for i in range(n):
        s = t[i]
        if t.count(s) > 1:
            maxi = max(maxi, 1)
        nr = 1
        for j in range(i + 1, n):
            s += t[j]
            nr += 1
            g = 0
            for h in range(n - nr + 1):
                if s == t[h:h + nr]:
                    g += 1
            if g > 1:
                maxi = max(nr, maxi)

    # print(maxi)
    pass
if __name__ == "__main__":
    # 示例：以 n=20 作为输入规模运行一次
    main(20)