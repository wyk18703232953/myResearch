def main(n):
    # 确定性生成输入数组 nums，长度为 n
    # 这里选择 nums[i] = (i + 1) * (i + 2)，保证为正整数且随 i 增长
    if n <= 0:
        print(0)
        return

    nums = [(i + 1) * (i + 2) for i in range(n)]

    out = nums[0]
    first = nums[0]
    for i in range(1, n):
        out = min(out, min(nums[i], first) // i)
    last = nums[-1]
    for i in range(n - 2, 0, -1):
        out = min(out, min(nums[i], last) // (n - 1 - i))
    print(out)


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 的规模做复杂度实验
    main(10)