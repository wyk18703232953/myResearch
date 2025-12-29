import random

def main(n):
    # 生成规模为 n 的测试数据，这里生成 1~1000 的随机整数
    a = [random.randint(1, 1000) for _ in range(n)]

    a.sort()
    sum1 = 0
    total_sum = sum(a)
    i = len(a) - 1
    c = 0

    # 根据原始逻辑执行
    while sum1 <= total_sum - sum1:
        sum1 += a[i]
        i -= 1
        c += 1

    print(c)


if __name__ == "__main__":
    # 示例：调用 main(10)，实际使用时可在外部按需调用 main(n)
    main(10)