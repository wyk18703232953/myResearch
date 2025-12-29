import random

def main(n: int):
    # 生成测试数据：长度为 n 的正整数数组 a
    # 保证元素为正数，避免整除时全部为 0
    a = [random.randint(1, 10**6) for _ in range(n)]

    k = min(a[0], a[-1]) // (n - 1)
    for i in range(1, n - 1):
        k = min(
            k,
            min(a[0], a[i]) // i,
            min(a[i], a[-1]) // (n - 1 - i)
        )
    print(k)

if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)