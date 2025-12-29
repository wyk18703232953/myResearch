import random

def main(n: int):
    # 1. 生成测试数据
    # 生成 m：让它在一个合理范围内，保证既有可能需要压缩，也有可能不需要
    # 这里令 a[i], b[i] 大致在 [1, 100]，m 在 [sum(b), sum(a)] 附近浮动
    a = []
    b = []
    for _ in range(n):
        ai = random.randint(1, 100)
        bi = random.randint(0, ai)  # 保证 a[i] - b[i] >= 0，便于模拟压缩
        a.append(ai)
        b.append(bi)

    sum_a = sum(a)
    sum_b = sum(b)
    # m 在 [sum_b, sum_a + 50] 之间随机，可能出现不可行情况
    m = random.randint(sum_b, sum_a + 50)

    # 2. 原始逻辑（去除 input，直接用生成的数据）
    diff = [a[i] - b[i] for i in range(n)]
    diff.sort(reverse=True)

    current_sum = sum_a
    i = 0
    while current_sum > m and i < n:
        current_sum -= diff[i]
        i += 1

    if i >= n and current_sum > m:
        print(-1)
    else:
        print(i)

if __name__ == "__main__":
    # 示例调用：可修改 n 测试不同规模
    main(5)