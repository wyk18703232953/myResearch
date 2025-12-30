import random

def main(n: int):
    # 生成测试数据：随机选择 a, b，满足题目逻辑的约束
    # 约束来自原逻辑：若 min(a, b) > 1 则直接 NO
    if n <= 0:
        return

    # 随机生成 a, b（1 到 n 之间），同时保证 min(a, b) == 1 的概率更高一些
    if random.random() < 0.7:
        # 强制其中一个为 1
        if random.random() < 0.5:
            a = 1
            b = random.randint(1, n)
        else:
            b = 1
            a = random.randint(1, n)
    else:
        a = random.randint(1, n)
        b = random.randint(1, n)

    # 原逻辑开始（去掉 input 和 exit，使用返回结束）
    if min(a, b) > 1:
        print('NO')
        return

    M = [[0] * n for _ in range(n)]

    if a == 1 and b == 1:
        if n == 1:
            print('YES')
            print('0')
            return
        if n == 2 or n == 3:
            print('NO')
            return
        for i in range(1, n):
            M[i - 1][i] = 1
            M[i][i - 1] = 1
    else:
        # assume b == 1
        s = n - max(a, b) + 1
        for i in range(s):
            for j in range(s):
                if i != j:
                    M[i][j] = 1
        if a == 1:
            for i in range(n):
                for j in range(n):
                    if i != j:
                        M[i][j] = 1 - M[i][j]

    print('YES')
    for i in range(n):
        print(''.join(map(str, M[i])))


if __name__ == "__main__":
    # 示例：运行若干不同规模的测试
    for size in [1, 2, 3, 4, 5]:
        print(f"n = {size}")
        main(size)
        print("-" * 20)