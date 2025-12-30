import random

def solve_case(n, k, s):
    p = (k + 2) // 2
    l = "RGB" * p
    res = n
    for i in range(n - k + 1):
        c = 0
        for j in range(0, k):
            c += (s[i + j] != l[j])
        res = min(res, c)

        c = 0
        for j in range(1, k + 1):
            c += (s[i + j - 1] != l[j])
        res = min(res, c)

        c = 0
        for j in range(2, k + 2):
            c += (s[i + j - 2] != l[j])
        res = min(res, c)
    return res


def main(n):
    # 这里根据 n 生成测试数据
    # 示例：假设测试用例数量 t = 5，k 在 [1, n] 内随机
    t = 5
    random.seed(0)
    results = []
    for _ in range(t):
        k = random.randint(1, n)
        s = ''.join(random.choice('RGB') for _ in range(n))
        ans = solve_case(n, k, s)
        results.append((n, k, s, ans))

    # 示例输出：返回所有测试用例及答案
    # 你也可以改为只返回答案列表等
    return results


if __name__ == "__main__":
    # 示例调用
    out = main(10)
    for n, k, s, ans in out:
        print(n, k, s, ans)