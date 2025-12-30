import random

def main(n: int) -> None:
    # 生成一个与规模 n 相关的测试数据：
    # 这里简单设为在 [0, n] 范围内的随机整数
    x = random.randint(0, n)

    # 原始逻辑：print(int(input()) // 2 * 3)
    result = x // 2 * 3

    print(result)


if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 的默认值
    main(100)