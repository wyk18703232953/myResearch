import random

def main(n: int):
    # 根据 n 生成测试数据：随机生成 a, b（保证在合理范围内）
    if n < 1:
        return

    # 为了模拟原题的约束，a, b 至少为 1，且不超过 n
    a = random.randint(1, max(1, n))
    b = random.randint(1, max(1, n))

    # 以下为原逻辑的封装
    if (a > 1 < b) or (a * b == 1 and 1 < n < 4):
        print('NO')
    else:
        z, o = ('01', '10')[a < b]  # 选择填充值顺序
        l = [[z] * n for _ in range(n)]
        for i in range(n):
            l[i][i] = '0'
        for i in range(n - a * b):
            l[i][i + 1] = l[i + 1][i] = o
        print('YES')
        print('\n'.join(map(''.join, l)))

if __name__ == "__main__":
    # 示例调用：可以修改 n 测试不同规模
    main(5)