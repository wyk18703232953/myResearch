import random

def solve(a, b):
    m = max(a, b)
    n = min(a, b)
    if n == 0:
        return 0
    if m == n:
        return 1
    elif m % n == 0:
        return m // n
    k = m // n
    return k + solve(n, m - n * k)

def main(n):
    # 生成 n 组测试数据，每组为两个正整数 a, b
    test_data = []
    for _ in range(n):
        # 控制数值规模，可根据需要调整上限
        a = random.randint(1, 10**6)
        b = random.randint(1, 10**6)
        test_data.append((a, b))

    # 执行并输出结果
    for a, b in test_data:
        print(solve(a, b))

if __name__ == "__main__":
    # 示例：运行规模为 5
    main(5)