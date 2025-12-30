import random

def main(n: int):
    # 1. 生成测试数据：长度为 n 的整数数组 a
    #   这里示例生成 [1, 100] 区间内的随机整数
    a = [random.randint(1, 100) for _ in range(n)]

    # 2. 按原逻辑处理
    a = sorted(a, reverse=True)
    s1 = 0
    s2 = sum(a)

    for i in range(len(a)):
        s1 += a[i]
        s2 -= a[i]
        if s1 > s2:
            break

    # 3. 输出结果
    print(i + 1)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)