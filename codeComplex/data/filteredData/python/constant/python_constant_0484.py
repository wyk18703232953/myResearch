import random

def main(n):
    # 根据规模 n 生成测试数据
    # 保证 n >= 1，k 为正整数
    if n <= 0:
        raise ValueError("n must be a positive integer")

    # 示例：令 k 在 [1, n*10] 范围内随机
    k = random.randint(1, n * 10)

    # 原逻辑：计算向上取整的 k / n
    ans = k // n
    if k % n:
        ans += 1

    print(ans)

if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)