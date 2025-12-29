import random

def main(n: int):
    # 生成规模为 n 的测试数据 Ab
    # 这里生成 0 到 10 之间的随机整数作为示例数据
    Ab = [random.randint(0, 10) for _ in range(n)]

    Un = []
    Al = [0]
    r = 0

    # 原始逻辑部分
    for i in range(n):
        Ab[i] = int(Ab[i])
        Al.append(max(Ab[i] + 1, Al[i]))

    for i in range(n, -1, -1):
        if Al[i - 1] < Al[i] - 1:
            Al[i - 1] = Al[i] - 1

    for i in range(n):
        Un.append(Al[i + 1] - Ab[i] - 1)
        r += Un[-1]

    print(r)


if __name__ == "__main__":
    # 示例调用：可以根据需要修改 n
    main(5)