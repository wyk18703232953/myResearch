import random

def main(n: int):
    # 1. 生成规模为 n 的测试数据：整数列表 l
    #   这里示例生成 [-n, n] 范围内的随机整数
    l = [random.randint(-n, n) for _ in range(n)]

    # 2. 原逻辑
    s = set(l)
    x = 0
    if x in s:
        print(len(s) - 1)
    else:
        print(len(s))

if __name__ == "__main__":
    # 示例：可以在这里调用 main 进行简单测试
    main(10)