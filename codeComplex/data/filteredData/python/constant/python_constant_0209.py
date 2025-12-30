import random

def main(n):
    # 生成测试数据：根据规模 n 随机生成三个整数
    # 这里假设每个数在 1~n 范围内，可根据需要调整生成规则
    k1 = random.randint(1, n)
    k2 = random.randint(1, n)
    k3 = random.randint(1, n)

    a = [k1, k2, k3]
    a = sorted(a)
    if a[0] == 1 or a.count(2) >= 2 or a.count(3) == 3:
        print("YES")
    elif a.count(4) == 2 and a.count(2) == 1:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    # 示例：使用 n = 10 调用
    main(10)