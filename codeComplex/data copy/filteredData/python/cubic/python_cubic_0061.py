def main(n):
    # 生成确定性字符串，长度为 n，字符由小写字母周期构成
    # 例如 n=10 -> 'abcdeabcde'
    if n <= 0:
        # print(0)
        pass
        return

    base = "abcdefghijklmnopqrstuvwxyz"
    x = "".join(base[i % len(base)] for i in range(n))
    l = len(x)
    m = 0

    for i in range(l - 1):
        f = i
        while True:
            idx = x[f + 1:].find(x[f])
            if idx == -1:
                break

            else:
                idx += f + 1
                c = 0
                ans = 0
                for j in range(idx, l):
                    if x[j] == x[i + c]:
                        ans += 1
                        c += 1

                    else:
                        break
                if m < ans:
                    m = ans
                f = idx
    # print(m)
    pass
if __name__ == "__main__":
    # 示例：输入规模为 20
    main(20)