import random

def main(n):
    # 生成测试数据
    # 约定：k 为 2~10 的随机整数，l 为 n 个 1~100 的随机整数
    k = random.randint(2, 10)
    l = [random.randint(1, 100) for _ in range(n)]

    # 原逻辑
    d = dict()
    c = set()
    l.sort()
    for i in range(n):
        if not d.get(l[i]):
            c.add(l[i])
            d.setdefault(l[i] * k, 1)
    print(len(c))


if __name__ == "__main__":
    # 示例：规模 n = 10
    main(10)