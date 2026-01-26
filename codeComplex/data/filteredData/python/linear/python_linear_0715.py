def main(n):
    # 生成确定性的输入数据：长度为 n 的整数数组
    # 这里使用简单的算术构造，使得同一个 n 下数据完全确定
    arr = [i * 2 + 3 for i in range(n)] if n > 0 else []

    # 如果 n 小于等于 1，原始逻辑中循环不会执行，此时 res 保持为无穷大
    # 为了有确定的返回值，这里约定当 n <= 1 时返回 0
    if n <= 1:
        # print(0)
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
    # 示例调用，可以根据需要修改 n 的值进行规模化实验
    main(10)