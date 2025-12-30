from itertools import accumulate
import random


def main(n: int) -> None:
    # 生成测试数据
    # n: 数组规模
    # 随机生成 m,k 和数组 a
    if n <= 0:
        return

    # 让 m 在 1..n 之间
    m = random.randint(1, n)
    # 生成 k 和数组元素，数值范围可根据需要调整
    k = random.randint(1, 10)
    a = [random.randint(0, 20) for _ in range(n)]

    # 原始逻辑开始
    als = []
    for i in range(m):
        ls = a[:]
        for j in range(n):
            if j % m == i:
                ls[j] -= k
        als.append(list(accumulate(ls)))

    ans = 0
    for i in range(m):
        ls = als[i]
        mn = 0
        anstmp = 0
        for j in range(n):
            if mn > ls[j]:
                mn = ls[j]
            if j % m == i:
                anstmp = max(anstmp, ls[j] - mn)
        ans = max(ans, anstmp)

    print(ans)


if __name__ == "__main__":
    # 示例：n = 10
    main(10)