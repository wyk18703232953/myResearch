import random

def main(n):
    # 生成测试数据
    # 约定：1 <= a < b <= n
    if n < 2:
        print(0)
        return

    a = random.randint(1, n - 1)
    b = random.randint(a + 1, n)

    # 生成 n 个随机整数
    arr = [random.randint(0, 1000) for _ in range(n)]

    # 原逻辑
    arr.sort()
    end_b = arr[b - 1]
    start_a = arr[b]
    if end_b < start_a:
        print(start_a - end_b)
    else:
        print(0)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)