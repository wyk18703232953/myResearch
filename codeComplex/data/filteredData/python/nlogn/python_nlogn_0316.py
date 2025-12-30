import random

def main(n: int):
    # 生成测试数据：长度为 n 的整数数组
    # 这里示例：在 [1, n] 范围内随机生成
    a = [random.randint(1, n) for _ in range(n)]

    w = sum(a[i] == i + 1 for i in range(n))
    if w >= n // 1000:
        print("Petr")
    else:
        print("Um_nik")


if __name__ == "__main__":
    # 示例：调用 main，规模可自行调整
    main(100000)