def main(n):
    # 映射含义：
    # n: 数组长度 n，参数 k 固定为 n//2（至少为 1）
    if n <= 1:
        # 处理规模极小的情况，保证算法逻辑仍然可执行
        k = 1
        arr = [1] * n
    else:
        k = max(1, n // 2)
        # 确定性构造数组：arr[i] = (i * 7 + 3) % 1000003
        arr = [(i * 7 + 3) % 1000003 for i in range(n)]

    l = []
    for i in range(n):
        l.append((arr[i], i))

    l.sort(reverse=True)

    dp = []
    x = 0
    for i in range(k):
        dp.append(l[i][1])
        x = x + l[i][0]

    print(x)
    dp.sort()
    dp = [-1] + dp

    length = len(dp)
    for i in range(1, length - 1):
        print(dp[i] - dp[i - 1], end=" ")
    print(n - 1 - dp[length - 2])


if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 的大小做时间复杂度实验
    main(10)