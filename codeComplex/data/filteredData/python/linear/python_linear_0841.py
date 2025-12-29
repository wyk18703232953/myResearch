import random

def solve_one_case(n, k, s):
    nxt = {'R': 'G', 'G': 'B', 'B': 'R'}
    res = []

    for start in ['R', 'G', 'B']:
        mis = []
        cur = start
        # 初始长度为 k 的窗口
        for j in range(k):
            mis.append(1 if s[j] != cur else 0)
            cur = nxt[cur]
        res.append(sum(mis))
        # 滑动窗口
        for j in range(k, n):
            res.append(res[-1] + int(s[j] != cur) - mis[j - k])
            mis.append(1 if s[j] != cur else 0)
            cur = nxt[cur]

    return min(res)


def main(n):
    """
    n: 字符串规模（长度）
    本函数内生成测试数据（T, 每个测试的 k, s），并执行原算法，打印结果。
    """
    random.seed(0)

    # 生成测试组数 T
    T = 5

    # 随机生成 T 组测试数据：(n_i, k_i, s_i)
    test_cases = []
    for _ in range(T):
        ni = n
        # 保证 1 <= k <= ni
        ki = random.randint(1, ni)
        s = ''.join(random.choice('RGB') for _ in range(ni))
        test_cases.append((ni, ki, s))

    # 按原逻辑对每组测试数据求解并输出
    for ni, ki, s in test_cases:
        ans = solve_one_case(ni, ki, s)
        print(ans)


if __name__ == "__main__":
    # 示例：以 n = 10 运行
    main(10)