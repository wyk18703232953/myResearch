import random

def main(n: int) -> None:
    # 生成测试数据：n 保持为参数传入的规模，s 为随机正整数
    # 这里令 s 在 [1, 10 * n] 范围内随机生成，可按需要调整
    s = random.randint(1, 10 * n)

    # 原始逻辑：计算向上取整的 s / n
    if s % n == 0:
        print(s // n)
    else:
        print(s // n + 1)


if __name__ == "__main__":
    # 示例：调用 main(10)，实际使用时可在此修改规模 n
    main(10)