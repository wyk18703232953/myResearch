import random

def main(n: int):
    # 生成一个规模为 n 的测试数据，这里简单用 [0, n] 范围内的随机整数
    x = random.randint(0, n)
    # 保留原逻辑：输出 int((x/2)*3)
    print(int((x / 2) * 3))

if __name__ == "__main__":
    # 示例：可以手动修改这里的 n 进行测试
    main(10)