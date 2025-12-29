import random

def main(n):
    # 根据规模 n 生成测试数据，这里例子为：在 [1, n] 中随机生成一个整数 x
    x = random.randint(1, n)
    # 原逻辑：print(int((x/2)*3))
    result = int((x / 2) * 3)
    print(result)

if __name__ == "__main__":
    # 示例：调用 main(100)，可按需修改规模 n
    main(100)