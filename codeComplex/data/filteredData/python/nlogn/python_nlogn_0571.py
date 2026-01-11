def main(n):
    if n <= 0:
        return
    # 构造一个确定性的父节点数组 a，表示一棵树
    # 这里构造方式：a[i] = i // 2 (i >= 2)，根节点 1 的父亲设为 0
    a = [0, 0] + [i // 2 for i in range(2, n + 1)]

    ans = [0] * (n + 1)
    for i in range(n, 1, -1):
        if ans[i] == 0:
            ans[i] = 1
        ans[a[i]] += ans[i]
    if n == 1:
        ans[1] = 1
    ans = ans[1:]
    ans.sort()
    # print(*ans)
    pass
if __name__ == "__main__":
    main(10)