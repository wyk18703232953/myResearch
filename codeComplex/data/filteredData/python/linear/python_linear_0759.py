import random

def main(n):
    # 生成规模为 n 的测试数据，这里示例为 [-10^9, 10^9] 范围内的随机整数
    a = [random.randint(-10**9, 10**9) for _ in range(n)]

    max_mod = 0
    max_i = -1
    for i in range(n):
        if a[i] >= 0:
            a[i] = -a[i] - 1
        if -a[i] > max_mod:
            max_mod = -a[i]
            max_i = i

    if n % 2 == 1:
        a[max_i] = -a[max_i] - 1

    print(' '.join(map(str, a)))


if __name__ == "__main__":
    # 示例：运行 main，规模可自行修改
    main(5)