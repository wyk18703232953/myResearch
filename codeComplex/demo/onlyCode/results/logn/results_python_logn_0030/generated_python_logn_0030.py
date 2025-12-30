import math
import random
from decimal import Decimal

def solve(l, r):
    if l == r:
        return 0

    val = 1
    while val * 2 <= r:
        val *= 2

    if val <= l:
        return solve(l - val, r - val)
    else:
        return 2 * val - 1


def main(n):
    """
    n 作为规模参数，用于生成测试数据。
    这里我们根据 n 生成一个区间 [l, r]，其中：
    - 1 <= l < r <= 2^n（上界会随 n 增大）
    """
    if n <= 1:
        upper = 2
    else:
        upper = 2 ** n

    # 确保有至少两个不同的数可选
    if upper < 2:
        upper = 2

    l = random.randint(0, upper - 1)
    r = random.randint(l + 1, upper)

    # 为了与原程序行为对应，保证 l <= r
    print(solve(l, r))


if __name__ == "__main__":
    # 示例：可以修改这里的 n 来测试不同规模
    main(10)