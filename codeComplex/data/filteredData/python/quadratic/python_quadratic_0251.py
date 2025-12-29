import random

def main(n):
    # 生成测试数据：根据 n 随机生成 a, b（可按需要修改生成策略）
    # 保证 1 <= a, b <= n，且尽量覆盖各种情况
    a = random.randint(1, n)
    b = random.randint(1, n)

    # 下面是原逻辑（去掉了 input()，改用生成的 a, b）
    if a > 1 and b > 1:
        print('NO')
        return

    if a == 1 and b == 1 and (n == 2 or n == 3):
        print('NO')
        return

    c = max(a, b)
    m = [[0] * n for _ in range(n)]

    # 构造初始链结构
    for i in range(n - c):
        m[i][i + 1] = 1
        m[i + 1][i] = 1

    # 若 b > 1，则取补图（除对角线外翻转 0/1）
    if b > 1:
        for i in range(n):
            for j in range(n):
                if i != j:
                    m[i][j] = 1 - m[i][j]

    print('YES')
    for i in range(n):
        print(''.join(map(str, m[i])))


if __name__ == "__main__":
    # 示例：调用 main(5) 进行一次运行
    main(5)