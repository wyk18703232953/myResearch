def main(n):
    # 生成确定性输入
    # a 为长度为 n 的数字字符列表，从 1 到 9 循环
    a = [str((i % 9) + 1) for i in range(n)]
    b = int("9" * n) if n > 0 else 0

    # 原算法逻辑
    a.sort(reverse=True)
    ans = ''
    while a:
        for i in range(len(a)):
            temp = ''
            x = ans + a[i] + temp.join(sorted(a[:i] + a[i+1:]))
            if int(x) <= b:
                ans += a[i]
                a = a[:i] + a[i+1:]
                break
    # print(int(ans))
    pass
if __name__ == "__main__":
    main(10)