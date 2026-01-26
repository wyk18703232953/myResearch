def main(n):
    # 生成确定性输入数据：长度为 n 的整数列表
    # 使用简单算术构造，保证可重复性
    a = [(i * 3 + 7) % (2 * n + 1) for i in range(n)]

    amin = min(a)
    for i in range(n):
        a[i] -= amin
    ans = amin % n
    cnt = 0
    while True:
        if a[ans] <= cnt:
            break
        ans = (ans + 1) % n
        cnt += 1
    # print(ans + 1)
    pass
if __name__ == "__main__":
    main(10)