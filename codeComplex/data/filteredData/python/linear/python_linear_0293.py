import random

def main(n: int):
    # 生成规模为 n 的测试数据：整数列表 a
    # 这里示例生成范围在 [-n, n] 的随机整数
    a = [random.randint(-n, n) for _ in range(n)]

    d = set(a)
    if 0 in a:
        print(len(d) - 1)
    else:
        print(len(d))


if __name__ == "__main__":
    # 示例：自行指定规模 n 进行测试
    main(10)