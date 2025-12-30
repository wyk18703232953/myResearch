import math
import random

def bi(n, k):
    MIN = 0
    MAX = n

    while MAX > MIN + 1:
        bn = (MIN + MAX) // 2
        if math.log2(k + 2 + bn) < bn + 1:
            MAX = bn
        elif math.log2(k + 2 + bn) == bn + 1:
            return bn
        else:
            MIN = bn

    if MAX + 1 <= math.log2(k + 2 + MAX):
        return MAX

    return MIN


def solve_one_case(n, k):
    if n == 1:
        if k == 1:
            return "YES 0"
        else:
            return "NO"

    if n == 2:
        if 1 <= k <= 2:
            return "YES 1"
        elif k == 3:
            return "NO"
        elif 4 <= k <= 5:
            return "YES 0"
        else:
            return "NO"

    if n <= 30 and k > (pow(4, n) - 1) // 3:
        return "NO"

    ans = bi(n, k)
    return f"YES {n - ans}"


def main(n):
    """
    n: 规模参数，用于生成测试数据。
       这里生成 n 组测试数据，每组 (ni, ki)。
    """
    random.seed(0)

    testcases = []
    for _ in range(n):
        # 生成 ni
        # 为了覆盖小规模和稍大规模，混合生成
        if random.random() < 0.4:
            ni = random.randint(1, 5)
        else:
            ni = random.randint(1, 50)

        # 生成 ki
        if ni <= 30:
            # 根据原代码中的约束来生成一部分合理范围内的 k
            max_k = (pow(4, ni) - 1) // 3
            if max_k < 1:
                max_k = 1
            # 有时生成超过上界的 k，看边界情况
            if random.random() < 0.3:
                ki = max_k + random.randint(1, 10)
            else:
                ki = random.randint(1, max_k)
        else:
            # 对于较大 ni，k 随机取一个不太大的数
            ki = random.randint(1, 10**6)

        testcases.append((ni, ki))

    # 输出结果
    for ni, ki in testcases:
        res = solve_one_case(ni, ki)
        print(res)


if __name__ == "__main__":
    # 示例：规模为 10
    main(10)