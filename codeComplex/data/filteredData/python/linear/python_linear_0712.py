def main(n):
    # 生成确定性输入数据：长度为 n 的整数数组
    # nums[i] = (i + 1) * 2 作为一个简单的、单调增长的构造
    if n <= 0:
        return
    nums = [(i + 1) * 2 for i in range(n)]

    out = nums[0]
    first = nums[0]
    for i in range(1, n):
        out = min(out, min(nums[i], first) // i)
    last = nums[-1]
    for i in range(n - 2, 0, -1):
        out = min(out, min(nums[i], last) // (n - 1 - i))
    # print(out)
    pass
if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 以进行规模化实验
    main(10)