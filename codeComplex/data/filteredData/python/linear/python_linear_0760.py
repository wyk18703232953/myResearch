import random

def main(n):
    # 生成测试数据：n个[-10^9, 10^9]之间的随机整数
    a = [random.randint(-10**9, 10**9) for _ in range(n)]

    # 原逻辑开始
    for i in range(n):
        if a[i] >= 0:
            a[i] = -a[i] - 1

    if n % 2 == 1:
        m = min(a)
        for i in range(n):
            if a[i] == m:
                a[i] = -a[i] - 1
                break

    # 输出结果
    print(*a)


if __name__ == "__main__":
    # 示例：运行规模为 n = 10
    main(10)