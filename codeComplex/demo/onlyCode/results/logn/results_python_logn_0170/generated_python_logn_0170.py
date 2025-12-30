import math
import random


def solve_naive(n, k):
    taken = set()
    current_cap = 0
    found = False
    while current_cap != n:
        for c in range(k, 1, -1):
            found = False
            if current_cap == 0:
                if c <= n:
                    current_cap += c
                    taken.add(c)
                    found = True
                    break
            else:
                if c not in taken and c - 1 <= n - current_cap:
                    current_cap += c - 1
                    taken.add(c)
                    found = True
                    break
        if not found:
            break
    return len(taken) if found else -1


def solve(n, k):
    if n == 1:
        return 0
    if k >= n:
        return 1
    else:
        disc = (3 - 2 * k) ** 2 - 8 * (n - k)
        if disc < 0:
            return -1
        t = (-math.sqrt(disc) + (2 * k) - 3) / 2
        if t == 0.0:
            return 2
        if t % 1 == 0:
            return 1 + int(t)
        else:
            return 2 + int(t)


def main(n):
    # 根据规模 n 生成测试数据：
    # 约定：n 为题目中的 n，k 在 [1, n] 范围内随机生成
    if n < 1:
        raise ValueError("n must be >= 1")

    k = random.randint(1, max(1, n))

    ans = solve(n, k)
    print(ans)


if __name__ == "__main__":
    # 示例：可以在此固定一个 n 用于本地测试
    main(10)