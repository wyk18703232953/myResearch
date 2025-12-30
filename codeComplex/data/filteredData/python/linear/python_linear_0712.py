import random

def main(n):
    # 1. 生成测试数据：长度为 n 的整数数组 nums
    # 根据原程序逻辑，需要 nums[0] 和 nums[-1]，且除以索引，避免 division by zero 问题
    # 这里生成 [1, 10^9] 范围内的随机整数
    if n <= 1:
        # 对于 n <= 1，原逻辑中循环不会执行，out = nums[0]
        nums = [random.randint(1, 10**9)]
    else:
        nums = [random.randint(1, 10**9) for _ in range(n)]

    # 2. 原逻辑计算
    out = nums[0]
    first = nums[0]
    # 前向部分：i 从 1 到 n-1
    for i in range(1, n):
        out = min(out, min(nums[i], first) // i)

    last = nums[-1]
    # 后向部分：i 从 n-2 到 1
    for i in range(n - 2, 0, -1):
        out = min(out, min(nums[i], last) // (n - 1 - i))

    # 3. 输出结果（可以根据需要同时输出测试数据）
    print(out)
    return out

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)