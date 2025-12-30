import random


def main(n: int):
    # 1. 生成规模为 n 的测试数据：非负整数数组 nums
    #   这里生成 [0, 10^9] 范围内的随机整数，可根据需要调整
    nums = [random.randint(0, 10**9) for _ in range(n)]

    nums.sort()
    margins = [num - i for i, num in enumerate(nums)]
    for m in margins:
        if m < 0:
            print("cslnb")
            return

    flag = False
    if len(nums) > 1 and nums[0] == nums[1]:
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
    # 示例：调用 main(5)
    main(5)