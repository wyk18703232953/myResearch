import random

def main(n):
    # 生成测试数据
    # n: 数组长度
    # 随机生成 k（避免为0）
    k = random.randint(1, max(2, n))

    # 生成长度为 n 的数组 l，元素为正整数
    l = [random.randint(1, 10 * n) for _ in range(n)]

    # 原逻辑
    l_sorted = sorted(l)
    res = set()
    for i in l_sorted:
        if i % k != 0:
            res.add(i)
        elif i // k not in res:
            res.add(i)

    # 输出结果长度（可根据需要返回或打印）
    print(len(res))
    return len(res)

if __name__ == "__main__":
    # 示例：规模为 10
    main(10)