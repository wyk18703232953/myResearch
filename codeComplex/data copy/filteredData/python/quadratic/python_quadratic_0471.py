def main(n):
    # 保证最小规模
    if n <= 0:
        return

    # 构造一个满足条件的确定性数据集
    # 使用一个简单可控的排列模式来生成 s
    s = [i % 3 for i in range(n)]

    # 根据 s 反推 a, b 使得原逻辑为 True
    a = [0] * n
    b = [0] * n

    for j in range(n):
        lj = 0
        rj = 0
        for i in range(n):
            if i < j and s[i] > s[j]:
                lj += 1
            elif i > j and s[i] > s[j]:
                rj += 1
        a[j] = lj
        b[j] = rj

    # 原始逻辑实现（去掉 input），保留算法结构
    s_check = [0] * n
    ans = True

    for i in range(n):
        ans = ans and a[i] <= i and b[i] <= (n - i - 1)
        s_check[i] = n - a[i] - b[i]

    def qwe(arr, j):
        l, r = 0, 0
        for i in range(len(arr)):
            if i < j and arr[i] > arr[j]:
                l += 1
            elif i > j and arr[i] > arr[j]:
                r += 1
        return l, r

    if ans:
        for i in range(n):
            l, r = qwe(s_check, i)
            ans = ans and a[i] == l and b[i] == r

    if ans:
        # print("YES")
        pass
        for i in range(n):
            # print(n - a[i] - b[i], end=" ")
            pass
        # print()
        pass

    else:
        # print("NO")
        pass
if __name__ == "__main__":
    # 示例调用：可以按需修改 n
    main(10)