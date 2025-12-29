import random

def main(n: int) -> None:
    # 这里根据 n 生成测试数据，这里测试数据就是一个整数 a
    # 为了可控，生成范围设为 [0, n]，你也可以按需修改
    a = random.randint(0, n)

    # 原逻辑：输入为 n 时输出 n + n // 2
    # 这里用生成的测试数据 a 代替原来的输入
    result = a + a // 2

    print(result)


if __name__ == "__main__":
    # 示例：调用 main，规模设为 10
    main(10)