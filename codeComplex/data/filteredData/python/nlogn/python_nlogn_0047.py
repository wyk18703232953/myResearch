import random

def main(n: int):
    # 生成规模为 n 的测试数据，这里生成 1~10 之间的随机整数
    l = [random.randint(1, 10) for _ in range(n)]
    
    l = sorted(l)
    if l[-1] == 1:
        l[-1] = 2
    else:
        l[-1] = 1
    l = sorted(l)
    print(*l)


if __name__ == "__main__":
    # 示例：可以在这里指定 n 进行测试
    main(5)