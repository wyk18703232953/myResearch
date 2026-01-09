def main(n):
    # 确定性生成 n 和 s
    # n 由参数决定，s 由简单确定性公式生成
    s = n * 2 + 5

    # 生成二维数组 arr，规模为 n
    # 每一行有两个整数 [a, b]
    # a 严格递减以便排序有意义；b 为与下标相关的简单函数
    arr = []
    for i in range(n):
        a = (n - i) * 3
        b = i * 2 + (i // 2)
        arr.append([a, b])

    arr = sorted(arr, reverse=True, key=lambda x: x[0])
    ans, c = 0, 0
    for i in range(n):
        if i != 0:
            c = arr[i - 1][0]
        if i == 0:
            ans = ans + s - arr[i][0]

        else:
            ans = ans + c - arr[i][0]
        if arr[i][1] >= ans:
            ans = ans + (arr[i][1] - ans)
    ans = ans + arr[n - 1][0]
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)