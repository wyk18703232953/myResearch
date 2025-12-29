import random

def main(n):
    # 根据 n 生成测试数据，这里示例为打印 -2 和 1 的位置对
    # 若需要使用随机数据，可在此处自行拓展
    for i in range(n // 3):
        print(-2, 1 + i * 2)
    for i in range(n - n // 3):
        print(1, i)

# 示例：调用 main(10)
if __name__ == "__main__":
    main(10)