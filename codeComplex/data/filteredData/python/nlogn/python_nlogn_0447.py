import random

def main(n):
    # 生成测试数据：
    # 1) 随机生成长度为 n 的数组 S，元素范围设为 [1, 2n]
    # 2) 随机选择一个位置作为 m 的位置，并保证 S 中至少有一个等于 m
    if n <= 0:
        return

    # 生成随机数组
    S = [random.randint(1, 2 * n) for _ in range(n)]

    # 随机选一个位置作为 m 的位置
    ind = random.randrange(n)
    m = S[ind]  # 将该位置元素作为 m

    # 以下是原逻辑的封装
    k = ind
    P = [0] * (n + 1)
    N = [0] * (n + 1)
    R = [0] * (n - k)
    L = [0] * (k + 1)

    # 处理左侧
    for i in range(k):
        if S[k - 1 - i] < m:
            L[k - 1 - i] = L[k - i] - 1
        else:
            L[k - 1 - i] = L[k - i] + 1

    # 处理右侧
    for i in range(n - k - 1):
        if S[k + 1 + i] > m:
            R[1 + i] = R[i] + 1
        else:
            R[1 + i] = R[i] - 1

    c = 0
    # 统计右侧前缀
    for el in R:
        if el >= 0:
            P[el] += 1
            if el == 0:
                N[el] += 1
        else:
            N[-el] += 1

    # 统计左侧前缀并累加答案
    for el in L:
        if el >= 1:
            c += N[el] + N[el - 1]
        else:
            c += P[-el] + P[-el + 1]

    print(c)


if __name__ == "__main__":
    # 示例：调用 main(10) 进行一次运行
    main(10)