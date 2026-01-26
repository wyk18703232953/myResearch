import math

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


def main(n):
    # n 作为测试规模：生成 t = n 组测试
    t = n
    results = []
    for i in range(t):
        # 确定性生成每组 (ni, ki)
        # ni 在 [2, 2+n] 范围内变化
        ni = 2 + (i % (n + 1))
        # ki 与 ni 有简单算术关系，保证覆盖不同数量级
        ki = 3 * (i + 1) + (ni * ni // 2)
        results.append(eval_(ni, ki))
    for res in results:
        # print(res)
        pass
if __name__ == "__main__":
    main(10)