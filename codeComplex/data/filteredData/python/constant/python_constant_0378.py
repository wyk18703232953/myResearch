import random

def main(n: int):
    # 随机生成符合题意范围的 a, b, c
    # 可根据需要调整范围（例如 0~n 或更大）
    a = random.randint(0, n)
    b = random.randint(0, n)
    c = random.randint(0, max(a, b))  # 保证 c 不会太离谱，也可能制造非法情况

    t = a + b - c
    if a >= n or b >= n or c > a or c > b or t >= n:
        print(-1)
    else:
        print(n - t)


if __name__ == "__main__":
    # 示例：调用 main，指定规模 n
    main(10)