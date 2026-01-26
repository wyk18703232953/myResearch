from collections import Counter
import string
import math
from fractions import Fraction

def array_int_from_generated(nums):
    return nums

def vary_from_generated_two(n, k):
    return n, k

def makedict(var):
    return dict(Counter(var))

def main(n):
    # 映射规则：
    # n -> 数组长度
    # k -> 子数组最小长度，设为 max(1, n//3)
    if n <= 0:
        return

    k = max(1, n // 3)

    # 生成确定性数组 num
    # 简单构造：num[i] = (i * 3 + 1) % (n + 7)
    # 确保有一定的变化且完全由 n 决定
    num = [(i * 3 + 1) % (n + 7) for i in range(n)]

    # 保持原始核心算法逻辑
    n_gen, k_gen = vary_from_generated_two(n, k)
    num_gen = array_int_from_generated(num)

    maxi = 0.0
    for i in range(n_gen):
        count = 1
        sumt = num_gen[i]
        for j in range(i + 1, n_gen):
            sumt += num_gen[j]
            count += 1
            if count >= k_gen:
                maxi = max(maxi, sumt / count)
    if k_gen == 1:
        # print(max(maxi, max(num_gen)))
        pass

    else:
        # print(maxi)
        pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n
    main(10)