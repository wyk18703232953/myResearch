import random

def solve_one(n, k, s):
    mini = n

    # pattern starting with 'R'
    test = "RGB" * (k // 3 + 5)
    for i in range(n - k + 1):
        count = 0
        for j in range(k):
            if s[i + j] != test[j]:
                count += 1
        mini = min(count, mini)

    # pattern starting with 'G'
    test = "GBR" * (k // 3 + 5)
    for i in range(n - k + 1):
        count = 0
        for j in range(k):
            if s[i + j] != test[j]:
                count += 1
        mini = min(count, mini)

    # pattern starting with 'B'
    test = "BRG" * (k // 3 + 5)
    for i in range(n - k + 1):
        count = 0
        for j in range(k):
            if s[i + j] != test[j]:
                count += 1
        mini = min(count, mini)

    return mini


def main(n):
    """
    n: 问题规模参数，用来生成测试数据。
       这里约定：
       - 随机生成 t 个测试用例，t = max(1, n // 10)
       - 每个测试的字符串长度为 len_s，区间为 [1, max(1, n)]
       - 对每个测试随机选择 k，1 <= k <= len_s
    """
    t = max(1, n // 10)
    colors = ['R', 'G', 'B']
    results = []

    for _ in range(t):
        len_s = random.randint(1, max(1, n))
        k = random.randint(1, len_s)
        s = ''.join(random.choice(colors) for _ in range(len_s))
        ans = solve_one(len_s, k, s)
        results.append(ans)

    # 模拟原程序逐行输出答案
    for x in results:
        print(x)


if __name__ == "__main__":
    # 示例：可根据需要更改 n
    main(30)