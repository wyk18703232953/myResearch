import random

def main(n: int):
    # 生成测试数据
    # 随机选择 c 和 序列 a 的元素范围为 [0, 500000]
    max_val = 500000
    c = random.randint(0, max_val)
    a = [random.randint(0, max_val) for _ in range(n)]

    res1 = [0] * (max_val + 1)
    res = 0
    for ai in a:
        res1[ai] = max(res1[ai], res1[c])
        res1[ai] += 1
        res = max(res, res1[ai] - res1[c])
    print(res + res1[c])


if __name__ == "__main__":
    # 示例：n 可根据需要修改或由外部调用 main(n)
    main(10)