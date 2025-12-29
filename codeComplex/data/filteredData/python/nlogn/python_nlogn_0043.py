import random

def main(n: int):
    # 1. 生成规模为 n 的测试数据：随机正整数，这里设定在 1~10 范围内
    t = [random.randint(1, 10) for _ in range(n)]

    # 2. 按原逻辑处理
    t.sort()
    if t[-1] == 1:
        t[-1] = 2
    else:
        t[-1] = 1
    t.sort()

    # 3. 输出结果
    print(*t)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)