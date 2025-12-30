import random

def main(n: int):
    # 根据 n 生成测试数据，这里直接使用 n 作为规模
    # 原始程序逻辑
    if n < 6:
        print(-1)
    else:
        print(1, 2)
        print(1, 3)
        print(1, 4)
        for i in range(4, n):
            print(2, i + 1)

    for i in range(n - 1):
        print(1, i + 2)


if __name__ == "__main__":
    # 示例：生成一个规模为 10 的测试
    main(10)