MAX = 1000

# 预处理 f 和 g
f = [0]
for i in range(1, MAX):
    f.append(f[i - 1] + (1 << (2 * i - 2)))

g = [0]
for i in range(1, MAX):
    g.append(g[i - 1] + (1 << i) - 1)


def solve_one(n, k):
    ans = False
    for i in range(1, n + 1):
        if k >= g[i]:
            if n >= MAX:
                return ("YES", n - i)
            elif k <= f[n] - ((1 << (i + 1)) - 1) * f[n - i]:
                return ("YES", n - i)
        if ans:
            break
    return ("NO",)


def main(n):
    """
    n 为规模，用于生成测试数据。
    这里的策略：
    - 生成 t = n 组测试
    - 第 i 组的 (n_i, k_i) = (i, 一些构造的 k)
    返回所有测试结果的字符串列表，用于检查。
    """
    results = []
    t = n

    for i in range(1, t + 1):
        # 构造测试数据 (n_i, k_i)
        # 让 n_i 随 i 变化，并在 MAX 上限附近也有取值
        n_i = min(MAX - 1, i)

        # 为了测试 YES/NO 情况，构造几种 k：
        # 交替使用比较小和比较大的 k
        if i % 3 == 1:
            # 小一些的 k
            k_i = g[1] if n_i >= 1 else 0
        elif i % 3 == 2:
            # 中等的 k
            k_i = g[min(n_i, 10)]

        else:
            # 较大的 k，尽量接近 f[n_i]
            k_i = f[n_i] if n_i < MAX else g[n_i % MAX]

        res = solve_one(n_i, k_i)
        if res[0] == "YES":
            results.append(f"YES {res[1]}")

        else:
            results.append("NO")

    # 输出结果
    for line in results:
        # print(line)
        pass

    return results


if __name__ == "__main__":
    # 示例：调用 main(10) 生成并测试 10 组数据
    main(10)