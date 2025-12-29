import random

def main(n: int):
    # 1. 生成规模为 n 的测试数据
    # 原程序只用到了 a[0] 和 a[1]，其余元素无意义
    # 这里按规模 n 生成长度为 n 的数组，但只保证前两个元素存在
    if n < 2:
        n = 2
    a = [random.randint(0, 10**9) for _ in range(n)]

    # 2. 原始逻辑开始
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
    # 示例：调用 main，传入规模 n
    main(10)