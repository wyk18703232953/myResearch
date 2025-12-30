import random

def main(n: int):
    # 根据规模 n 生成测试数据：n 为原始的 n，m 随机生成但不参与后续逻辑
    m = random.randint(1, max(1, n))

    # 以下是原程序逻辑，将 input() 替换为由参数 n/m 提供的数据
    a = []
    b = []
    nn = n  # 使用 nn 模拟原始代码里的 n

    while nn >= 0:
        a.append(4)
        nn -= 4
        b.append(5)

    a.append(5)
    b.append(5)

    print(*a, sep="")
    print(*b, sep="")

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)