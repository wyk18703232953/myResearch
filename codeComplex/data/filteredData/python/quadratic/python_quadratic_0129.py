import random

def main(n: int):
    # 生成测试数据：
    # a 为不同整数的种类数，b 为数组长度
    a = n
    b = n * 3  # 可根据需要调整规模关系

    # 在 1..a 范围内随机生成 b 个数，保证每个 1..a 至少出现一次
    base = list(range(1, a + 1))
    extra_len = max(0, b - a)
    extra = [random.randint(1, a) for _ in range(extra_len)]
    arr = base + extra
    random.shuffle(arr)

    # 原始逻辑
    mn = float("inf")
    for i in range(1, a + 1):
        mn = min(mn, arr.count(i))

    print(mn)


if __name__ == "__main__":
    # 示例：规模设为 5，可自行修改
    main(5)