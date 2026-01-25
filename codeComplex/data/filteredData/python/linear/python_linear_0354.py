def main(n):
    # 生成长度为 n 的数字字符串，确定性构造
    if n <= 0:
        print(0)
        return
    s = ''.join(str((i * 7 + 3) % 10) for i in range(n))

    n_len = len(s)
    l = [[0, 0, 0] for _ in range(n_len)]
    ans = 0
    x = int(s[0]) % 3
    if x == 0:
        ans += 1
    else:
        l[0][x] = 1
    for i in range(1, n_len):
        x = int(s[i]) % 3
        if x == 0:
            ans += 1
            continue
        if l[i - 1][3 - x] > 0:
            ans += 1
            l[i][3 - x] = 0
            l[i][x] = 0
        else:
            if l[i - 1][x] != 0:
                l[i][1] = 1
                l[i][2] = 1
            else:
                l[i][x] = 1
    print(ans)


if __name__ == "__main__":
    main(10)