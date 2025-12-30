from math import sqrt
import random

def main(n):
    # 根据规模 n 生成测试数据：
    # 这里我们让 k 与 n 同数量级，确保有一定随机性与覆盖面
    # k 至少为 1
    k = max(1, int(sqrt(n)) + random.randint(0, 5))

    # 原逻辑开始
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
        ub = k * (k - 1) // 2
        p = lambda x: ub - x * (x - 1) // 2
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


if __name__ == "__main__":
    # 示例：调用 main(n)，可根据需要修改 n
    main(10)