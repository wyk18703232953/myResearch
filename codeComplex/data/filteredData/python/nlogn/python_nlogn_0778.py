import sys
import random
import math

sys.setrecursionlimit(100000)


def main(n):
    # 生成测试数据
    # 约定：k 在 [1, n] 内随机取值，nums 为长度为 n 的严格递增序列
    if n <= 0:
        return

    # 随机选择 k，1 <= k <= n
    k = random.randint(1, n)

    # 生成严格递增的 nums
    # 先生成 n 个正增量，再做前缀和
    increments = [random.randint(1, 10) for _ in range(n)]
    nums = []
    cur = 0
    for inc in increments:
        cur += inc
        nums.append(cur)

    # 原逻辑开始
    diff = []
    for i, j in zip(nums, nums[1:]):
        diff.append(j - i)

    diff.sort()
    # 注意：当 n == k 时，n - k == 0，sum([]) == 0
    ans = sum(diff[:(n - k)])

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main，n 为规模，可按需修改
    main(10)