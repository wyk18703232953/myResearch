import random

def main(n: int):
    # 生成测试数据
    # N: 数组长度，K: 分组数(1 <= K <= N)
    N = n
    if N <= 0:
        return
    K = random.randint(1, N)
    # 生成一个长度为 N 的整数数组 a
    # 数值范围可自行调整
    a = [random.randint(0, 1000) for _ in range(N)]

    # 原始逻辑
    diff = []
    for i in range(1, N):
        diff.append([i, a[i] - a[i - 1]])

    diff = sorted(diff, key=lambda x: -x[1])
    res = max(a) - min(a)

    k = 0
    while k < K - 1 and k < len(diff):
        res -= diff[k][1]
        k += 1

    print(res)


if __name__ == "__main__":
    # 示例：使用 n=10 运行
    main(10)