import random

def main(n):
    # 生成测试数据：n 组 (k1, k2, k3)
    # 这里假定每个数在 1~n 范围内，可根据需要调整
    test_cases = []
    for _ in range(n):
        k1 = random.randint(1, n)
        k2 = random.randint(1, n)
        k3 = random.randint(1, n)
        test_cases.append((k1, k2, k3))

    # 对每组测试数据执行原逻辑并输出
    for k1, k2, k3 in test_cases:
        l = [k1, k2, k3]
        if 1 in l:
            print("YES")
        elif l.count(2) >= 2:
            print("YES")
        elif l.count(3) == 3:
            print("YES")
        elif sorted(l) == [2, 4, 4]:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    # 示例：生成并处理 5 组数据
    main(5)