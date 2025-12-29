import random

def main(n: int):
    # n 用作随机数种子，保证相同 n 时测试数据可复现
    random.seed(n)
    
    # 根据 n 生成测试数据
    # 这里约定：
    #   x, y, z 在 [-n, n] 范围内
    #   t1, t2, t3 在 [1, n] 范围内（时间单价为正）
    x = random.randint(-n, n)
    y = random.randint(-n, n)
    z = random.randint(-n, n)
    t1 = random.randint(1, n if n > 0 else 1)
    t2 = random.randint(1, n if n > 0 else 1)
    t3 = random.randint(1, n if n > 0 else 1)

    time1 = abs(x - y) * t1
    time2 = (abs(x - y) + abs(z - x)) * t2 + 3 * t3

    if time2 <= time1:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)