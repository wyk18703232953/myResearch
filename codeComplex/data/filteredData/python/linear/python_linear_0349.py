import random

def main(n):
    # 生成测试数据：随机生成 m 和 m 对区间 (a, b)
    # 这里 m 与 n 同规模，可根据需要调整
    m = max(1, n)  # 保证至少有 1 个测试区间

    l = []
    r = []
    for _ in range(m):
        # 随机生成区间 [a, b]，1 <= a <= b <= n
        a = random.randint(1, n)
        b = random.randint(a, n)
        l.append(a)
        r.append(b)

    # 原始逻辑：根据 n 输出 0/1 串
    for i in range(n):
        if i % 2 == 0:
            print(0, end='')
        else:
            print(1, end='')

if __name__ == "__main__":
    # 示例调用，可以修改 n 测试不同规模
    main(10)