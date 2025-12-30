import random

def main(n):
    # 根据 n 生成测试数据，这里生成 n 个范围在 [-10^9, 10^9] 的随机整数
    a = [random.randint(-10**9, 10**9) for _ in range(n)]

    # 原逻辑
    for i in range(n):
        if a[i] >= 0:
            a[i] = -a[i] - 1

    if n % 2 == 1:
        i = a.index(min(a))
        a[i] = -a[i] - 1

    a_str = list(map(str, a))
    print(" ".join(a_str))


if __name__ == "__main__":
    # 示例：可在此处指定规模 n
    main(10)