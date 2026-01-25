def main(n):
    # 生成长度为 n 的数字字符串，字符在 '0'~'9' 间确定性循环
    if n <= 0:
        print(0)
        return
    s = ''.join(str(i % 10) for i in range(n))
    length = len(s)
    ans = 0
    c = 0
    l = []
    for i in range(length):
        a = int(s[i]) % 3
        if a == 0:
            ans += 1
            c = 0
            l = []
        else:
            if c == 0:
                l.append(int(s[i]))
                c += 1
            elif c == 1:
                if (a + l[0]) % 3 == 0:
                    ans += 1
                    c = 0
                    l = []
                else:
                    c += 1
            else:
                ans += 1
                c = 0
                l = []
    print(ans)


if __name__ == "__main__":
    main(10)