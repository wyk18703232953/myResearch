import random

def main(n: int):
    # 根据规模 n 生成测试数据，这里模拟原始代码中的 n,m 输入
    # 原始逻辑只用到 n，m 可任意生成，这里令 m = n 的随机偏移
    m = n + random.randint(-n, n)

    # 原始逻辑开始
    print(n * "8")
    print((n - 1) * "1" + "2")


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)