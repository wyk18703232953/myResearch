import random

def main(n: int):
    # 生成测试数据：n 个 1~1000 的随机整数
    a = [random.randint(1, 1000) for _ in range(n)]

    # 原逻辑
    a.sort()
    s = 0
    c = 0
    total = sum(a)
    while s <= total:
        s += a.pop()
        c += 1

    print(c)


if __name__ == "__main__":
    # 示例：运行规模为 10 的测试
    main(10)