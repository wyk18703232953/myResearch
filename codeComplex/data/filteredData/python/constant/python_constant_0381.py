import random

def main(n):
    # 生成测试数据：
    # a, b 在 [0, 2n] 范围内随机
    # c 在 [0, min(a, b)] 中随机，以增加合法情况概率
    # n 本身作为题目中的 n
    a = random.randint(0, 2 * n)
    b = random.randint(0, 2 * n)
    c = random.randint(0, min(a, b)) if min(a, b) > 0 else 0

    t = a + b - c
    if c > a or c > b:
        print(-1)
        return
    if n - t >= 1:
        print(n - t)
    else:
        print(-1)


if __name__ == "__main__":
    # 可以在此处指定规模 n
    main(10)