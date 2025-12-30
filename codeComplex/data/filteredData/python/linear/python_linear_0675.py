import random

def main(n):
    # 1. 生成规模为 n 的测试数据：随机整数列表
    #    你可以根据需要调整数值范围
    numbers = [random.randint(0, 100) for _ in range(n)]

    # 2. 原逻辑实现
    l = []
    for j in numbers:
        if not l or j % 2 != l[-1]:
            l.append(j % 2)
        else:
            l.pop()

    if len(l) < 2:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    # 示例：规模为 10
    main(10)