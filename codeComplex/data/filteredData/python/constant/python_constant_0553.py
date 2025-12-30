import random

def main(n: int):
    # 生成测试数据：
    # n: 给定规模
    # m: 1 到 n 之间的随机整数
    # k, l: 0 到 n 之间的随机整数
    if n <= 0:
        raise ValueError("n 必须为正整数")

    m = random.randint(1, n)
    k = random.randint(0, n)
    l = random.randint(0, n)

    # 原始逻辑
    cnt = (k + l + m - 1) // m
    if cnt * m > n:
        result = -1
    else:
        result = cnt

    # 输出结果（如需返回结果可改为 return result）
    print(result)


if __name__ == "__main__":
    # 示例：运行规模为 10 的测试
    main(10)