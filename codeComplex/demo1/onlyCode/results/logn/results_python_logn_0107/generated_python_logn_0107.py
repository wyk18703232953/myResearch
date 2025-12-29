import random

def main(n: int):
    # 生成规模为 n 的测试数据：两个整数 a0, a1
    # 这里示例：在区间 [0, 2^n - 1] 内随机生成两个数
    if n <= 0:
        a0, a1 = 0, 0
    else:
        upper = (1 << n) - 1
        a0 = random.randint(0, upper)
        a1 = random.randint(0, upper)

    # 原逻辑开始
    a = [a0, a1]
    n_val = a[0] ^ a[1]
    x = bin(n_val)[2:]
    f = 0
    for i in range(len(x)):
        if x[i] == '1':
            f = 1
            break
    l = len(x) - i
    s = 0
    for i in range(l):
        s += 2 ** i
    if f == 0:
        s = 0

    print(s)

if __name__ == "__main__":
    # 示例：使用 n=10 运行
    main(10)