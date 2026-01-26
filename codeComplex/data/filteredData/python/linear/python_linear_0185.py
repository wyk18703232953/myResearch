def main(n):
    # n 表示数组长度，生成一个确定性的数组
    a = [i % 10 for i in range(1, n + 1)]
    s = sum(a)
    new = 0
    i = 0
    if n == 0:
        # print(0)
        pass
        return
    while i < n and 2 * (new + a[i]) < s:
        new += a[i]
        i += 1
    # print(i + 1 if i < n else n)
    pass
if __name__ == "__main__":
    main(10)