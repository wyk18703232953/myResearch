import random

def main(n):
    # 随机生成 1 <= k < n 的测试数据
    if n <= 1:
        print("")  # 原逻辑对 n<=1 不太适用，这里输出空串
        return

    k = random.randint(1, n - 1)

    d = (n - k) // 2 + 1
    x = ['1' if (i + 1) % d == 0 else '0' for i in range(n)]
    print(''.join(x))


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)