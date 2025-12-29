import random

def main(n: int):
    # 生成规模为 n 的测试数据，这里简单地让各参数在 [-n, n] 范围内随机
    x = random.randint(-n, n)
    y = random.randint(-n, n)
    z = random.randint(-n, n)
    t1 = random.randint(1, max(1, n))  # 避免为 0
    t2 = random.randint(1, max(1, n))
    t3 = random.randint(1, max(1, n))

    if abs(x - z) * t2 + abs(x - y) * t2 + t3 * 3 <= t1 * abs(x - y):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    # 示例：可在此处指定规模 n
    main(10)