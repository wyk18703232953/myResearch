import random

def main(n: int):
    # 生成测试数据
    # 随机选取 k，范围 1 ~ max(1, n//2)
    k = random.randint(1, max(1, n // 2))
    # 生成 n 个随机正整数，范围 1 ~ 1e9
    l = [random.randint(1, 10**9) for _ in range(n)]

    # 原逻辑
    res = set()
    for i in l:
        if i // k not in res or i % k != 0:
            res.add(i)

    # 输出结果
    print(len(res))


if __name__ == "__main__":
    # 示例：规模为 10
    main(10)