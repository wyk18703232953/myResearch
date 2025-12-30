import random

def main(n):
    # 生成测试数据
    # n: 数组规模
    # m: 操作次数，取 1..n 之间随机值
    # k: 分组大小，取 1..n 之间随机值
    m = random.randint(1, n)
    k = random.randint(1, n)
    # 生成递增的 arr，模拟原题中常见的“已排序位置数组”
    arr = sorted(random.sample(range(1, n + 1), m))

    modulo = 0
    tmp = 0
    op = 1
    cur = (arr[0] - 1) // k
    for i in range(m):
        if (arr[i] - 1 - modulo) // k != cur:
            modulo += tmp
            cur = (arr[i] - 1 - modulo) // k
            tmp = 0
            op += 1
        tmp += 1
    print(op)


if __name__ == "__main__":
    # 示例：可以根据需要修改规模 n
    main(10)