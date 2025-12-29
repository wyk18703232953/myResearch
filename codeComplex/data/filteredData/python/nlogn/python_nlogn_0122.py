import random

def main(n):
    # 生成测试数据
    # n: 数组大小
    # m: 目标值，取一个与 n 同级别的数
    # k: 初始值，小于等于 m
    m = random.randint(max(1, n // 2), max(1, n * 2))
    k = random.randint(0, m)
    list1 = [random.randint(1, 10) for _ in range(n)]

    # 原逻辑开始
    list1.sort(reverse=True)
    c = 0
    i = 0

    while k < m and i < n:
        k += list1[i] - 1
        i += 1
        c += 1

    if k >= m:
        print(c)
    else:
        print(-1)

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)