def main(n):
    # 生成确定性输入：长度为 n 的数字字符串列表
    # 使用 i % 10 构造，保证每个字符都是 '0' 到 '9'
    a = [int(str(i % 10)) for i in range(n)]
    smm = 0
    for i in range(n):
        smm += a[i]
    ans = "NO"
    sm = smm
    for div in range(2, n + 1):
        sm = smm
        if not sm % div:
            sm //= div
            f = 0
            s = 0
            for i in range(n):
                s += a[i]
                if s == sm:
                    s = 0
                    f += 1
            if f == div:
                ans = "YES"
                break
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)