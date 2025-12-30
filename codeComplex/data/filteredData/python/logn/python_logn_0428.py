import math
import random


def eval_(n, k):
    level = 0.5 * math.log2(3 * k + 1)
    if n > 30:
        cond = (level - n) > 0
    else:
        cond = (3 * k + 1) > 4 ** n
    if cond:
        return "NO"
    elif n == 2 and k == 3:
        return "NO"
    else:
        level = math.floor(level)
        if n > 5:
            temp = 1 + 0.5 * math.log2(3 * (k - 1) + 1)
            if n > temp:
                return "YES " + str(n - 1)
            else:
                return "YES  0"
        else:
            delta = 2 ** (n - level) * (2 ** level - 1) * (4 ** (n - level) - 1) // 3
            start = (4 ** level - 1) // 3
            if k <= (start + delta):
                return "YES " + str(n - level)
            else:
                return "YES " + str(n - level - 1)


def main(t):
    """
    t: 测试数据规模（测试组数）
    自动生成 t 组 (n, k)，并打印 eval_(n, k) 的结果。
    """
    random.seed(0)
    for _ in range(t):
        # 生成 n：1 到 50 之间
        n = random.randint(1, 50)
        # 生成 k：1 到 4^n 之间，避免明显越界导致大量 "NO"
        # 对于较大的 n，4^n 非常大，这里限制上界，防止整数过大
        max_k = min(4 ** n if n <= 15 else 10 ** 7, 10 ** 9)
        k = random.randint(1, max_k)
        print(eval_(n, k))


if __name__ == "__main__":
    # 示例：生成 5 组测试数据
    main(5)