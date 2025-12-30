import random

def main(n):
    # 根据 n 生成一个测试输入值，这里示例为从 1 到 n 的随机整数
    x = random.randint(1, n)

    # 原逻辑开始（将原来的 n 替换为 x）
    x += 1
    if x == 1:
        result = 0
    elif x % 2 == 0:
        result = x // 2
    else:
        result = x

    print(result)


if __name__ == "__main__":
    # 示例：调用 main，规模 n 为 100
    main(100)