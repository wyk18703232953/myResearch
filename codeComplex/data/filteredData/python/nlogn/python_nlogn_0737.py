def main(n):
    if n <= 0:
        return

    # 生成确定性的 nums，长度为 n
    # 构造方式：nums[i] = i // 2，保证有重复元素且随 n 增长有规律
    nums = [i // 2 for i in range(n)]

    nums.sort()
    margins = [num - i for i, num in enumerate(nums)]
    for m in margins:
        if m < 0:
            print("cslnb")
            return
    flag = False
    if len(nums) > 1:
        if nums[0] == nums[1]:
            flag = True
    for a, b, c in zip(nums, nums[1:], nums[2:]):
        if b == c:
            if a == b or b - a == 1:
                print("cslnb")
                return
            if flag:
                print("cslnb")
                return
            flag = True

    margin = sum(margins)
    if margin % 2 == 1:
        print("sjfnb")
    else:
        print("cslnb")


if __name__ == "__main__":
    # 示例：以 n = 10 运行一次，用于时间复杂度实验
    main(10)