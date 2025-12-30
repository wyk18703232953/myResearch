a = [0 for _ in range(100)]
b = [0 for _ in range(100)]
for i in range(1, 100):
    a[i] = a[i - 1] * 2 + 1
    b[i] = b[i - 1] + a[i]


def calc(x: int) -> int:
    return (4 ** x - 1) // 3


def main(n: int):
    """
    n 为测试规模，这里生成 n 组 (n_i, k_i) 测试数据并依次处理。
    生成规则示例：
      - n_i 在 [1, 40] 内循环取值（覆盖 n>35 与 n<=35 场景）
      - k_i 在 [1, calc(n_i)+5] 内取值（包含 <=calc(n_i) 和 >calc(n_i) 的情况）
    """
    tests = []
    for i in range(1, n + 1):
        ni = 1 + (i % 40)  # 避免 0，且让 ni 在 1..41 之间分布，包含 >35
        limit = calc(ni)
        # 生成 k：穿插合法/非法范围
        if i % 3 == 1:
            ki = max(1, limit // 2)          # 中间值
        elif i % 3 == 2:
            ki = limit + 1                   # > calc(ni)
        else:
            ki = max(1, limit - i % 5)       # 接近上界
        tests.append((ni, ki))

    for n_val, k in tests:
        if n_val > 35:
            print("YES " + str(n_val - 1))
        elif 1 + calc(n_val - 1) >= k:
            print("YES " + str(n_val - 1))
        elif calc(n_val) < k:
            print("NO")
        else:
            for i in range(1, n_val + 1):
                if b[i] <= k <= calc(n_val) - (2 ** (i + 1) - 1) * calc(n_val - i):
                    print("YES " + str(n_val - i))
                    break
            else:
                print("NO")


if __name__ == "__main__":
    # 示例：运行规模为 10 的测试
    main(10)