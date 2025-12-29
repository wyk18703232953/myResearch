import random

def main(n: int):
    # 根据 n 生成测试数据（此处直接使用 n 作为原始输入规模）
    x = n

    # 原逻辑：n = n + n // 2
    x = x + x // 2

    print(x)


if __name__ == "__main__":
    # 示例：调用 main(10)，实际使用时可按需修改 n
    main(10)