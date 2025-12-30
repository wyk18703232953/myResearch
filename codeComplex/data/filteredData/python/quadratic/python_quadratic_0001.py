import math
import random


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def lcm(a, b):
    return (a * b) / gcd(a, b)


def main(n: int):
    # 生成测试数据
    # 约定：r 为正整数，a 为严格递增的整数序列，长度为 n
    if n <= 0:
        return

    r = random.randint(1, 10)  # 半径
    a = []
    cur = 0
    for _ in range(n):
        # 每个位置与前一个位置间隔在 [1, 2*r] 之间
        cur += random.randint(1, 2 * r)
        a.append(cur)

    ans = []
    ans.append(r)
    for i in range(1, n):
        ymax = r
        for j in range(i):
            if abs(a[j] - a[i]) <= 2 * r:
                ymax = max(
                    ymax,
                    ans[j] + math.sqrt(4 * r * r - (a[i] - a[j]) ** 2),
                )
        ans.append(ymax)

    # 输出与原逻辑一致：仅输出 ans（中间结果）
    print(*ans)


if __name__ == "__main__":
    # 示例：规模 n = 10，可按需修改
    main(10)