from __future__ import division
import random


def solve(a, m):
    n = len(a)
    a = a[::-1]          # 原代码中读入后就做了 [::-1]
    cur, ans = 2, -1

    for i in range(n - 2):
        cur = max(cur, i + 2)
        for j in range(cur, n):
            if a[i] - a[j] < 1:
                cur += 1
                continue

            if a[i] - a[j] > m:
                break

            cur += 1
            v = (a[i] - a[j - 1]) / (a[i] - a[j])
            ans = max(ans, v)
    return ans


def main(n):
    # 生成测试数据：
    # n: 数组长度
    # m: 根据数组范围设置一个差值上限
    random.seed(0)
    # 生成递增数组，保证有一定的差值空间
    a = sorted(random.randint(0, 1000) for _ in range(n))
    m = max(1, (a[-1] - a[0]) // 2)

    ans = solve(a, m)
    print(ans)


if __name__ == "__main__":
    # 示例：规模为 10
    main(10)