from collections import deque
import random

def main(n):
    """
    规模参数 n 用于生成测试数据：
    - 数组长度 = n
    - 查询数量 q = n
    - 数组为 1..n 的随机排列（保证有唯一最大值）
    - 查询 mj 为 1..(2*n) 中的随机整数，用于测试 mj > len(ab) 的情况
    """
    if n <= 0:
        return

    # 生成测试数据
    q = n
    nums = list(range(1, n + 1))
    random.shuffle(nums)  # 随机排列
    queries = [random.randint(1, 2 * n) for _ in range(q)]

    # 以下为原逻辑的无 input() 改写
    nums = deque(nums)
    m = max(nums)  # 最大值

    # ab 存储在最大值到达队首之前的所有对 (a, b)
    ab = []
    while nums[0] < m:
        ab.append([nums[0], nums[1]])
        if nums[0] > nums[1]:
            # 将第二个元素移到队尾
            nums.append(nums[1])
            del nums[1]
        else:
            # 将第一个元素移到队尾
            nums.append(nums[0])
            del nums[0]

    # 处理查询
    # nums 的当前状态：最大值在首位，其余元素每一步循环右移一位（不含最大值）
    for mj in queries:
        if mj <= len(ab):
            a, b = ab[mj - 1]
        else:
            # 周期性位置：第一个是最大值 m，第二个从剩余 nums[1:] 中循环选择
            idx = (mj - len(ab) - 1) % (len(nums) - 1) + 1
            a, b = m, nums[idx]
        print(f"{a} {b}")


# 示例：当此文件作为脚本运行时，用某个固定规模测试
if __name__ == "__main__":
    main(10)