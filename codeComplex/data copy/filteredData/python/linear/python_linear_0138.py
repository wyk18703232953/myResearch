def main(n):
    # n 表示数组 a 的长度
    if n <= 0:
        # print(0)
        pass
        return

    # 确定性构造输入数组 a：例如 a[i] = i % 7
    a = [i % 7 for i in range(n)]

    b = []
    maxi = 0
    for i in range(n):
        maxi = max(maxi, a[i] + 1)
        b.append(maxi)

    c = []
    count = b[-1]
    for i in range(n - 1, -1, -1):
        if count - 1 >= b[i]:
            count -= 1
            c.append(count)

        else:
            c.append(count)
    c = c[::-1]

    ans = 0
    for i in range(n):
        ans += (c[i] - a[i] - 1)
    # print(ans)
    pass
if __name__ == "__main__":
    # 示例：使用 n = 10 进行一次实验
    main(10)