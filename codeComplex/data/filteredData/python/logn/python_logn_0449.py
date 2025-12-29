squareMoves = []


def precompute():
    top = 10 ** 18
    prev = 0

    while prev <= 30 * top:
        squareMoves.append(prev)
        prev = 1 + 4 * prev


def getAns(k, n):
    low = 0
    high = 0
    a = 1
    b = 1
    i = 1

    while i <= n:
        low += a
        high += a + b * squareMoves[n - i]

        if high >= k:
            if low > k:
                return -1
            return i

        a = 2 * a + 1
        b = 2 * a - 1
        i += 1

    return -1


def main(n):
    """
    n: 规模参数，用于生成测试数据和控制用例数量。
       这里约定生成 n 个测试用例，第 i 个用例为：
       - n_i = i
       - k_i = i * i  （可根据需要调整生成规则）
    函数返回值为每个用例的结果列表。
    """

    precompute()

    results = []
    for i in range(1, n + 1):
        cur_n = i
        cur_k = i * i
        tmpN = min(cur_n, len(squareMoves))
        ans = getAns(cur_k, tmpN)
        if ans == -1:
            results.append("NO")
        else:
            results.append(f"YES {cur_n - ans}")
    return results


if __name__ == "__main__":
    # 示例：运行规模 n=5，并打印结果
    for line in main(5):
        print(line)