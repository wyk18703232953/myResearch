import random

def main(n: int):
    # 这里的 n 既作为规模参数，也直接作为原程序中的输入值使用
    # 如果需要基于规模生成随机测试数据，可在此修改为：
    # x = random.randint(0, n)
    x = n

    if x == 0:
        print(0)
    else:
        if x % 2 == 0:
            print(x + 1)
        else:
            print((x + 1) // 2)


if __name__ == "__main__":
    # 示例：基于规模 10 生成一次测试并运行
    main(10)