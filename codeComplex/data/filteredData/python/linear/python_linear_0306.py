import random

def main(n: int):
    # 生成测试数据：随机整数，范围可根据需要调整
    # 这里生成 n 个在 [1, n^2] 范围内的整数
    arr = [random.randint(1, n * n) for _ in range(n)]

    # 原逻辑
    for i in range(n):
        arr[i] = (arr[i] - i) // n + (1 if (arr[i] - i) % n > 0 else 0)
    print(arr.index(min(arr)) + 1)


if __name__ == "__main__":
    # 示例：调用 main(10)，可根据需要修改 n
    main(10)