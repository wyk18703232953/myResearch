import random

def main(n: int):
    # 生成测试数据：长度为 n 的正整数数组
    # 这里假设元素范围在 1 到 10^9 之间，可按需调整
    arr = [random.randint(1, 10**9) for _ in range(n)]

    res = float('inf')
    for i in range(1, n):
        res = min(res, min(arr[i], arr[0]) // i)
    for i in range(n - 1):
        res = min(res, min(arr[i], arr[n - 1]) // (n - 1 - i))
    print(res)


if __name__ == "__main__":
    # 示例调用：可修改 n 测试不同规模
    main(10)