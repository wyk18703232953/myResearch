MAX = 1000
f = [0]
for i in range(1, MAX):
    f.append(f[i - 1] + (1 << (2 * i - 2)))

g = [0]
for i in range(1, MAX):
    g.append(g[i - 1] + (1 << i) - 1)


def run_case(n, k):
    ans = False
    for i in range(1, n + 1):
        if k >= g[i]:
            if n >= MAX:
                # print("YES %d" % (n - i))
                pass
                ans = True
            elif k <= f[n] - ((1 << (i + 1)) - 1) * f[n - i]:
                # print("YES %d" % (n - i))
                pass
                ans = True
        if ans:
            break
    if not ans:
        # print("NO")
        pass


def main(n):
    # 将 n 映射为测试用例数量和每个用例的 n, k 规模
    t = max(1, n)  # 测试用例数量
    for case_id in range(1, t + 1):
        # 为每个测试用例构造 (n_case, k_case)，完全由 case_id 和 n 决定
        n_case = max(1, min(MAX - 1, (case_id * 7 + n) % MAX))
        # 让 k_case 与 g 的规模相关，保证覆盖不同分支
        base = (case_id * 13 + n * 17) % MAX
        if base == 0:
            base = 1
        # 使用 g[base] 和一些算术构造一个确定性的 k
        k_case = g[base] + (case_id * case_id + n) // 3
        run_case(n_case, k_case)


if __name__ == "__main__":
    main(10)