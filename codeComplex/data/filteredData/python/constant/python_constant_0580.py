import random

def main(n: int):
    # 根据规模 n 生成测试数据 (x, y)，取值范围为 [1, n]
    x = random.randint(1, n)
    y = random.randint(1, n)

    d1 = abs(x - 1) + abs(y - 1)
    d2 = abs(n - x) + abs(n - y)

    result = "White" if d1 <= d2 else "Black"
    print(result)

if __name__ == "__main__":
    # 示例：调用 main，规模 n 可自行修改
    main(8)