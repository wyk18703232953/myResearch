import random

def main(n: int):
    # 根据规模 n 生成测试数据：
    # 这里为演示起见，设 n 为人数，s 为 [1, 10*n] 范围内的随机整数
    if n <= 0:
        raise ValueError("n must be positive")

    s = random.randint(1, 10 * n)

    # 原始逻辑：给定 n, s，输出 ceil(s / n)
    if s % n == 0:
        result = s // n
    else:
        result = s // n + 1

    # 按原程序行为，仅打印结果
    print(result)

if __name__ == "__main__":
    # 示例：调用 main(10)，实际使用时可修改为任意正整数规模
    main(10)