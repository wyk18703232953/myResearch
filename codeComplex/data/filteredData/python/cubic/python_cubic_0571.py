def main(n):
    # 确定性生成输入
    # a 为由数字字符组成的列表，长度为 n，按简单模式生成
    digits = [str((i * 7 + 3) % 10) for i in range(n)]
    a = digits
    # b 为一个与 n 相关的整数上界，保证随 n 单调增加
    # 使用一个确定性的线性构造
    b = int("9" * n) if n > 0 else 0

    # 原算法逻辑
    a = sorted(a, reverse=True)
    ans = ''
    while len(a) > 0:
        for i in range(len(a)):
            tmp = ans + a[i] + ''.join(sorted(a[:i] + a[i + 1:]))
            if int(tmp) <= b:
                ans += a[i]
                a = a[:i] + a[i + 1:]
                break
    # print(ans)
    pass
if __name__ == "__main__":
    main(5)