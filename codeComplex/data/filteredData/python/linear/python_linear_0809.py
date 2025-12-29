import random

def main(n):
    # 生成测试数据
    # n: 整体规模，这里用作 m 的最大值和 special 值域的上界参考
    if n <= 0:
        return

    # 随机生成参数
    m = random.randint(1, n)              # special 的个数
    k = random.randint(1, max(1, n // 2)) # 分组参数，至少为 1

    # 生成 m 个 [1, n] 范围内的互不相同的整数，并排序
    special = sorted(random.sample(range(1, max(n, m) + 1), m))

    # 以下是原始逻辑
    numOn = 0
    numOps = 0
    while numOn < m:
        numOps += 1
        op = ((special[numOn] - numOn - 1) // k) * k + k + numOn + 1
        while numOn < m and special[numOn] < op:
            numOn += 1

    print(numOps)


if __name__ == "__main__":
    # 示例：规模设为 100
    main(100)