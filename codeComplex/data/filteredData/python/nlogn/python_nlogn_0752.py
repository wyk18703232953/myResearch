import random

def solve(n, a):
    a = sorted(a)
    if n == 1:
        return a[0] > 0 and a[0] % 2 == 1
    same_count = 0
    for i in range(n - 1):
        if a[i] == a[i + 1] == 0:
            return False
        if i < n - 2 and a[i] + 1 == a[i + 1] == a[i + 2]:
            return False
        if a[i] == a[i + 1]:
            same_count += 1
    if same_count > 1:
        return False
    return (sum(a) - n * (n - 1) // 2) % 2 == 1


def main(n):
    # 生成规模为 n 的测试数据
    # 为保证与原题约束相符，生成非负整数序列
    # 这里生成范围在 [0, 2n] 内的随机数据
    a = [random.randint(0, 2 * n) for _ in range(n)]

    r = solve(n, a)
    if r:
        print('sjfnb')
    else:
        print('cslnb')


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)