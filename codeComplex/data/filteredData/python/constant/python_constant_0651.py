from collections import defaultdict, Counter
from copy import deepcopy
import random

def main(n):
    # 1. 生成测试数据
    # n 为数组长度，元素值范围 [1, max(2, n//2)]
    # 随机选择 c 保证在逻辑上有意义
    if n <= 0:
        return

    max_val = max(2, n // 2)
    a = [random.randint(1, max_val) for _ in range(n)]
    c = random.choice(a)

    # 2. 原逻辑，无 input()
    nums = defaultdict(lambda: [0])
    freq = Counter()
    minus = 0

    for x in a:
        if x == c:
            minus += 1
        else:
            freq[x] += 1
            nums[x].append(freq[x] - minus)

    tot = minus
    suff = deepcopy(nums)

    for key in nums:
        for j in range(len(nums[key]) - 2, 0, -1):
            suff[key][j] = max(suff[key][j], suff[key][j + 1])

    freq = Counter()
    ans = tot
    for x in a:
        if x == c:
            continue
        freq[x] += 1
        ans = max(ans, suff[x][freq[x]] - nums[x][freq[x]] + 1 + tot)

    print("n =", n)
    print("array a =", a)
    print("c =", c)
    print("answer =", ans)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)