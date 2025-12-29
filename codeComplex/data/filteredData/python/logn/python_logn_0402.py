from math import sin, tan, cos
import random


def solve(n, m, k, l):
    lb, rb = 0, n // m + 1
    while rb - lb > 1:
        mid = (lb + rb) >> 1
        if mid * m - k >= l:
            rb = mid
        else:
            lb = mid

    return rb if lb != n // m else -1


def main(n):
    # 根据规模 n 生成测试数据：
    # 令 m 在 [1, n] 范围内，k 在 [0, n]，l 在 [0, n]
    if n <= 0:
        return -1

    random.seed(0)
    m = random.randint(1, max(1, n))
    k = random.randint(0, n)
    l = random.randint(0, n)

    ans = solve(n, m, k, l)
    print(ans)


if __name__ == "__main__":
    # 示例：使用 n=100 作为规模
    main(100)