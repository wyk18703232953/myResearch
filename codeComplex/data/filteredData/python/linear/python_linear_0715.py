def main(n):
    # 生成确定性输入数据：长度为 n 的整数数组
    # 示例构造：arr[i] = (i + 1) * 3
    arr = [(i + 1) * 3 for i in range(n)]

    if n <= 1:
        # 原代码在 n <= 1 时 for 循环不会更新 res，保持 inf
        res = float('inf')
        # print(res)
        pass
        return

    res = float('inf')
    for i in range(1, n):
        res = min(res, min(arr[i], arr[0]) // i)
    for i in range(n - 1):
        res = min(res, min(arr[i], arr[n - 1]) // (n - 1 - i))
    # print(res)
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 规模做实验
    main(10)