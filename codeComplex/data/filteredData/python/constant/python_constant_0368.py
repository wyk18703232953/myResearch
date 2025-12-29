import random

def main(n: int):
    # 生成测试数据 a, b, c, n，保证为非负整数
    # 这里简单设置为：随机生成 a, b, c，n 不小于 a + b + c
    a = random.randint(0, n)
    b = random.randint(0, n)
    c = random.randint(0, n)
    total = a + b + c
    if total > n:
        # 调整 n 以保证有一定概率存在可行解
        n = total + random.randint(0, n)

    # 原逻辑
    a_adj = a - c
    b_adj = b - c
    remain = n - a_adj - b_adj - c

    if remain >= 1 and a_adj >= 0 and b_adj >= 0:
        print(remain)
    else:
        print(-1)


if __name__ == "__main__":
    # 示例：调用 main，规模 n 可自行调整
    main(100)