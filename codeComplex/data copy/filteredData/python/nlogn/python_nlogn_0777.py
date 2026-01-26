def main(n):
    # n 表示序列长度
    if n <= 0:
        # print("NO")
        pass
        return

    # 生成一个确定性的“山峰”序列：严格递增后严格递减，无重复
    # 例：n=5 -> [1,2,3,2,1]
    peak = (n + 1) // 2
    inc_part = list(range(1, peak + 1))
    dec_part = list(range(peak - 1, 0, -1))
    nums = inc_part + dec_part
    if len(nums) > n:
        nums = nums[:n]

    has_dups = (len(nums) > len(set(nums)))
    mx = nums.index(max(nums))
    if has_dups or nums[:mx + 1] != sorted(nums[:mx + 1]) or nums[mx:] != sorted(nums[mx:], reverse=True):
        # print("NO")
        pass

    else:
        # print("YES")
        pass
if __name__ == "__main__":
    main(10)