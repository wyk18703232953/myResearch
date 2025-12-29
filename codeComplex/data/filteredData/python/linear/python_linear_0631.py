MAX = 1000

# 预处理 f, g
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
                return f"YES {n - i}"
            else:
                if k <= f[n] - ((1 << (i + 1)) - 1) * f[n - i]:
                    return f"YES {n - i}"
        if ans:
            break
    return "NO"


def main(n):
    """
    n 为规模参数，生成 n 组 (n_i, k_i) 测试数据并输出结果。
    这里采用简单的测试数据生成方案，可根据需要修改：
      - n_i 在 [1, n] 内变化
      - k_i 为与 g 和 f 有关的一些值，以覆盖多种情况
    """
    t = n  # 生成 n 组测试
    print(t)

    for i in range(1, t + 1):
        # 构造一个 n_i：在 1..n 中循环
        ni = i

        # 构造一个 k_i：尝试在 g[1..min(ni, MAX-1)] 范围附近取值
        if ni < MAX:
            base_idx = min(ni, MAX - 1)
            # 三种情况混合：小于 g[base_idx]，等于 g[base_idx]，略大于
            if i % 3 == 1:
                ki = max(0, g[base_idx] - i)  # 小一点
            elif i % 3 == 2:
                ki = g[base_idx]             # 恰好
            else:
                ki = g[base_idx] + i         # 大一点
        else:
            # 对于很大的 ni，令 k 成为一个相对较大的数
            ki = g[MAX - 1] + i * 10

        print(ni, ki)
        print(solve_one(ni, ki))


if __name__ == "__main__":
    # 示例调用，按需要修改 n
    main(10)