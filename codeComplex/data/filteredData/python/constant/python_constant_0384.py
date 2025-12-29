import random

def main(n: int):
    # 根据规模 n 生成测试数据
    # 约束：a, b, c, n 都为正整数，且保证 a, b, c < n 的数量级
    a = random.randint(1, max(1, n))
    b = random.randint(1, max(1, n))
    c = random.randint(1, max(1, n))
    # 原代码中 n 是输入，这里我们用传入的 n 作为规模和逻辑中的 n

    if c > a or c > b or (a + b) - c >= n:
        print(-1)
    else:
        print(n - ((a + b) - c))


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)