import random

def main(n):
    # 随机生成 a, b，满足 0 <= a < b < n
    if n < 2:
        raise ValueError("n 必须 >= 2 才能保证有至少两个元素进行差值计算")
    a = random.randint(0, n - 2)
    b = random.randint(a + 1, n - 1)

    # 生成长度为 n 的随机测试数据 h
    # 这里生成 0~1000 的随机整数，可按需求调整范围
    h = [random.randint(0, 1000) for _ in range(n)]
    h.sort()

    # 输出与原程序逻辑对应的结果
    print(h[b] - h[b - 1])


if __name__ == "__main__":
    # 示例：运行规模为 10 的测试
    main(10)