def nine(p):
    s = ''
    for _ in range(p):
        s += '9'
    return int(s)


def prosh(p):
    ans = 0
    for i in range(1, p + 1):
        ans += nine(i) * 9
    return ans


def solve_one(n, k):
    l = [0] * 29
    for i in range(19):
        e = nine(19 - i)
        l[i] = int(k / e)
        k -= l[i] * e

        if k <= 0:
            break
        if i == 18 or k % e > prosh(19 - i - 1):
            l[i] += 1
            break

    otv = 0
    for i in range(19):
        otv += 10 ** (19 - i) * l[i]

    return max(n - otv + 1, 0)


def main(n):
    """
    生成规模为 n 的测试数据并运行算法。
    这里示例：生成 n 对 (n_i, k_i)，然后计算结果列表返回。
    可根据需要调整测试数据生成方式。
    """
    results = []
    for i in range(1, n + 1):
        # 示例测试数据：
        # 让 n_i 从 1 增长到 10^6，k_i 从 1 增长到 10^18 范围内变化
        n_i = 10 ** 6  # 或者用其他与规模 n 相关的构造
        k_i = i * (10 ** 12)
        res = solve_one(n_i, k_i)
        results.append(res)
    return results


if __name__ == "__main__":
    # 示例：运行 main(5) 并打印结果
    ans_list = main(5)
    for v in ans_list:
        print(v)