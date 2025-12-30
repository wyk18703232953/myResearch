import random

def main(n: int):
    # 生成测试数据：随机生成 case 以及 (n, k) 对
    # 此处将原始代码中每个测试用例的 n 固定为传入的 n，仅随机生成 k
    case = max(1, n)  # 测试用例数量，可以根据需要调整规则
    test_cases = []
    for _ in range(case):
        # 生成一个 k，范围可按需求调整
        # 这里设为 1 到 10^9 之间的随机数
        k = random.randint(1, 10**9)
        test_cases.append((n, k))

    # 执行原逻辑
    for (n_i, k_i) in test_cases:
        f = [0] * 32
        g = [0] * 32
        success = False
        n, k = n_i, k_i
        ans = n

        # 第一段逻辑
        for i in range(1, n):
            f[i] = f[i - 1] * 4 + 1
            if f[i] >= k:
                success = True
                break

        # 第二段逻辑
        for i in range(1, n + 1):
            if k < (1 << i) - 1:
                break
            k = k - (1 << i) + 1
            ans = ans - 1

        # 第三段逻辑
        for i in range(n - 1, ans - 1, -1):
            if i >= 32 or (i and f[i] == 0):
                success = True
                break
            g[i] = 1 if i == n - 1 else g[i + 1] * 2 + 3
            k = k - f[i] * g[i]
            if k <= 0:
                success = True
                break

        print("YES %d" % ans if success else "NO")


if __name__ == "__main__":
    # 示例调用：规模 n 可在此处调整
    main(10)