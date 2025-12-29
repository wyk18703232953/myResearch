import random
from collections import Counter

mod = 1000000007


def main(n):
    """
    n: 题目中的 n（需要的人数规模）
    自动生成 m 和 arr 测试数据，并运行原逻辑，返回 days。
    """
    # 生成测试数据：
    # 保证 m >= n，避免原逻辑直接输出 0
    m = max(n, 1) + random.randint(0, 3 * max(n, 1))

    # 生成 m 个整数，范围 [1, max(1, n//2)]，模拟原题中的“类别”
    if n <= 1:
        value_range = 1
    else:
        value_range = n // 2
    arr = [random.randint(1, value_range) for _ in range(m)]

    # 原逻辑开始（去掉输入部分，使用 n, m, arr）

    if n > m:
        days = 0
    else:
        c = Counter(arr)
        d1 = list(sorted(c.values()))

        days = 0
        for i in range(1, 101):
            d = d1.copy()
            people = 0
            done = False

            while True:
                if people >= n:
                    days = i
                    done = True
                    break
                if len(d) == 0:
                    break

                curr = d[-1] // i
                d.pop()
                people += curr

            if done:
                days = i

    # 输出与原程序相同的结果
    print(days)
    return days


if __name__ == "__main__":
    # 示例运行：传入一个规模 n
    main(10)