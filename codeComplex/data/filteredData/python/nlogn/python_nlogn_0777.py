import random

def main(n: int):
    # 生成规模为 n 的测试数据：整数列表 nums
    # 这里生成 [1, n] 范围内的随机整数，可根据需要自行修改
    nums = [random.randint(1, n) for _ in range(n)]

    has_dups = (len(nums) > len(set(nums)))
    mx = nums.index(max(nums))
    if has_dups or nums[:mx+1] != sorted(nums[:mx+1]) or nums[mx:] != sorted(nums[mx:], reverse=True):
        print("NO")
    else:
        print("YES")


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)