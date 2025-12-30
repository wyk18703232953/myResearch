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
    t: 测试数据规模，表示生成多少组 (n, k) 测试并输出结果。
    这里随机生成每组数据的 n, k：
      - n 在 [1, 40] 内
      - k 在 [1, 4^n] 内（避免过大导致溢出）
    """
    random.seed(0)
    for _ in range(t):
        n = random.randint(1, 40)
        # 为避免 4**n 过大，这里当 n > 30 时限制 k 上界
        if n <= 30:
            k_max = 4 ** n
        else:
            k_max = 4 ** 30
        k = random.randint(1, k_max)
        print(eval_(n, k))


if __name__ == "__main__":
    # 示例：生成 5 组随机测试
    main(5)