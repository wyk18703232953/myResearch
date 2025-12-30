import random

def main(n):
    # 生成测试数据
    # n 表示数组长度，q 这里设为 n（也可以按需调整）
    q = n
    # 生成一个长度为 n 的随机排列，确保存在最大值 m 且唯一
    nums = list(range(1, n + 1))
    random.shuffle(nums)

    m = max(nums)
    ab = []

    # 模拟操作，直到最大值到达队首
    while nums[0] < m:
        ab.append([nums[0], nums[1]])
        if nums[0] > nums[1]:
            # 将 nums[1] 移到队尾
            nums.append(nums.pop(1))
        else:
            # 将 nums[0] 移到队尾
            nums.append(nums.pop(0))

    # 生成 q 个查询，这里简单设为 1..q
    queries = list(range(1, q + 1))

    # 回答查询
    for mj in queries:
        if mj <= len(ab):
            a, b = ab[mj - 1]
        else:
            a, b = m, nums[(mj - len(ab) - 1) % (len(nums) - 1) + 1]
        print(str(a) + " " + str(b))


if __name__ == "__main__":
    # 示例运行，n 可按需调整
    main(10)