def main(n):
    # 根据规模 n 生成确定性输入数据 a，长度为 n
    # 构造方式：a[i] = (i % 5) - 2，产生负数、零和正数的混合
    a = [(i % 5) - 2 for i in range(n)]

    b = [abs(x) for x in a]
    if n == 1:
        ans = a[0]
    elif all(x > 0 for x in a) or all(x < 0 for x in a):
        b.sort()
        ans = sum(b) - 2 * b[0]

    else:
        ans = sum(b)
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)