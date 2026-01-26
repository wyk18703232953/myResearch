def main(n):
    # 生成确定性字符串，长度由 n 控制
    # 这里使用重复的周期模式，保证对不同 n 的可重复性
    if n <= 0:
        s = ""

    else:
        base = "abcdefghijklmnopqrstuvwxyz"
        s = "".join(base[i % len(base)] for i in range(n))

    pb = 0
    lenght = len(s) - 1
    w = []
    while lenght != 0:
        ss = s[pb:pb + lenght]
        w.append(ss)
        if pb + lenght == len(s):
            pb = 0
            lenght -= 1

        else:
            pb += 1

    for i in range(0, len(w) - 1):
        for j in range(i + 1, len(w)):
            if w[i] == w[j]:
                # print(len(w[i]))
                pass
                return
    # print(0)
    pass
if __name__ == "__main__":
    # 示例：使用 n=20 作为输入规模
    main(20)