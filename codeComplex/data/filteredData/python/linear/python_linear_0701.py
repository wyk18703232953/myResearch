import random

def main(n):
    # 根据规模 n 生成测试数据
    # 原程序中：n, v = [int(item) for item in input().split()]
    # 这里设定 v 的规模与 n 同级别，可根据需要调整生成规则
    v = random.randint(0, n * n)

    x = 0
    c = 0
    for i in range(1, n):
        if x < n - i:
            delta = min((n - i), v - x)
            c += i * delta
            x += delta
        x -= 1

    print(c)


if __name__ == "__main__":
    # 示例：运行规模为 10 的测试
    main(10)