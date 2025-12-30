from math import sqrt
import random

def main(n):
    # 根据规模 n 生成测试数据：
    # 这里将 k 设为与 n 同数量级的一个值（至少为 2）
    # 你可以按需要调整生成策略
    k = max(2, int(sqrt(max(1, n))) + random.randint(0, 3))

    # 原始逻辑开始
    ub = k * (k + 1) // 2 - k + 1

    if n > ub:
        result = -1
    elif n == ub:
        result = k - 1
    elif n == 1:
        result = 0
    elif n <= k:
        result = 1
    else:
        st = 1
        en = k - 1
        target = n - 1
        ub2 = k * (k - 1) // 2
        p = lambda x: ub2 - x * (x - 1) // 2
        ans = -1

        while st <= en:
            md = (st + en) // 2
            if p(md) <= target:
                ans = md
                en = md - 1
            else:
                st = md + 1

        if p(ans) == target:
            result = k - ans
        else:
            result = k - ans + 1

    print(result)
    return result

if __name__ == "__main__":
    # 示例：调用 main，规模 n 自行设定
    main(10)