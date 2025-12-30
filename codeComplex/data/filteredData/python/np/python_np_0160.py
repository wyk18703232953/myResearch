import random

def main(n):
    # 生成测试数据
    # 题意：有 n 道题，每道题一个难度值，选择若干题，
    # 要求总难度在 [l, r] 内，且最大难度与最小难度之差至少为 x
    # 这里根据 n 构造一组合理规模的测试数据
    # l, r, x 与 nums 都可以按需调整生成策略

    # 生成难度数组 nums，取值范围 [1, 1000]
    nums = [random.randint(1, 1000) for _ in range(n)]
    nums.sort()

    # 生成 l, r, x
    total_sum = sum(nums)
    # 保证区间不要太大也不要太小
    l = max(1, total_sum // 4)
    r = min(total_sum, total_sum // 2 + total_sum // 4)
    x = max(1, (nums[-1] - nums[0]) // 2)  # 要求差值至少为整体跨度的一半

    ans = 0

    def recurse(i, s, cnt):
        nonlocal ans
        if i == n:
            if not cnt:
                return
            if l <= s <= r and abs(cnt[-1] - cnt[0]) >= x:
                ans += 1
            return
        # 不选第 i 个
        recurse(i + 1, s, cnt[:])
        # 选第 i 个
        cnt.append(nums[i])
        recurse(i + 1, s + nums[i], cnt[:])

    recurse(0, 0, [])

    # 输出结果以及本次生成的测试数据，方便查看
    print("n =", n)
    print("nums =", nums)
    print("l =", l, "r =", r, "x =", x)
    print("answer =", ans)


if __name__ == "__main__":
    # 示例：运行规模 n = 10
    main(10)