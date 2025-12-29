import random

def main(n):
    # 根据规模 n 生成测试数据
    # 保证 k 为正整数，范围可根据需要调整，这里设为 [1, n^2]
    if n <= 0:
        raise ValueError("n 必须为正整数")
    k = random.randint(1, max(1, n * n))

    # 原逻辑：对给定 n, k 进行二分查找，求满足 c * n >= k 的最小整数 c
    a, b, c = 0, k, 0

    while a < b:
        c = (a + b) // 2
        if c * n < k:
            a = c + 1
        else:
            b = c

    print(a)


if __name__ == "__main__":
    # 示例：调用 main，规模 n 可自行修改
    main(10)