def main(n):
    # n 表示数组长度
    if n <= 0:
        return

    # 确定性生成输入数组：a[i] = i - n//2
    a = [i - n // 2 for i in range(n)]

    for i in range(n):
        if a[i] >= 0:
            a[i] = -a[i] - 1
    x = min(a)

    if len(a) % 2 == 1:
        for i in range(n):
            if a[i] == x:
                a[i] = -a[i] - 1
                break
    # print(*a)
    pass
if __name__ == "__main__":
    main(10)