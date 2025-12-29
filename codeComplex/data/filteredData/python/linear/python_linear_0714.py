import random

def main(n: int):
    # 生成测试数据：长度为 n 的整数数组 A
    # 这里示例使用 1 到 10^9 的随机整数
    A = [random.randint(1, 10**9) for _ in range(n)]

    k = 10 ** 10
    if n >= 2:
        for i in range(1, n - 1):
            k = min(k, min(A[0], A[i]) // i)
            k = min(k, min(A[-1], A[i]) // (n - i - 1))
        k = min(k, min(A[0], A[-1]) // (n - 1))
    else:
        # 若 n < 2，原逻辑中最后一步会除以 (n-1)=0，不合理。
        # 这里根据实际需求进行约定：n<2 时返回 0。
        k = 0

    print(k)


if __name__ == "__main__":
    # 示例：调用 main，规模为 10
    main(10)