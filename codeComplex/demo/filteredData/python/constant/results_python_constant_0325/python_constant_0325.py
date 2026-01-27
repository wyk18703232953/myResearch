def f(a, ind):
    if a[ind] == 0:
        return -1
    k = a[ind] // 14
    x = a[ind] % 14
    b = a[:]
    b[ind] = 0
    for j in range(14):
        b[j] += k
    for j in range(ind + 1, ind + x + 1):
        j1 = j % 14
        b[j1] += 1
    res = 0
    for j in range(14):
        if b[j] % 2 == 0:
            res += b[j]
    return res


def main(n):
    # 生成长度为14的测试数据，与规模 n 相关
    # 这里示例：a[i] = (i + 1) * n
    a = [(i + 1) * n for i in range(14)]

    ans = 0
    for i in range(14):
        cur = f(a, i)
        ans = max(ans, cur)
    # print(ans)
    pass
if __name__ == "__main__":
    # 示例：调用 main(10)，实际使用时按需修改 n
    main(10)