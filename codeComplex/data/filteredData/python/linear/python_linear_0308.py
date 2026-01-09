def main(n):
    # 生成确定性输入：长度为 n 的整数数组 a
    # 这里选择 a[i] = (i * 2 + 3) % (n + 5) + i // 2，保证有变化且完全确定
    a = [(i * 2 + 3) % (n + 5) + i // 2 for i in range(n)]

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