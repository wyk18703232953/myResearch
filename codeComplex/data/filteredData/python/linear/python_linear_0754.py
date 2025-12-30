import random

def main(n):
    # 生成测试数据：n个随机整数，范围可自行调整
    a = [random.randint(-10**9, 10**9) for _ in range(n)]

    # 原逻辑开始
    for i in range(n):
        if a[i] >= 0:
            a[i] = -a[i] - 1
    x = min(a)

    if len(a) % 2 == 1:
        for i in range(n):
            if a[i] == x:
                a[i] = -a[i] - 1
                break

    print(*a)


if __name__ == "__main__":
    # 示例：调用 main，规模 n 可在此修改
    main(10)