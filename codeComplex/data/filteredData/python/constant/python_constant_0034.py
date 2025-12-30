import random

def main(n: int):
    # 根据 n 生成测试数据：这里直接使用 n 作为原程序中的输入
    # 如果需要更复杂的生成方式，可以在此根据 n 随机生成或构造数据
    value = n
    result = value + value // 2
    print(result)


if __name__ == "__main__":
    # 示例：按规模生成一个测试值并调用 main
    # 这里简单设定为：测试值等于规模 n 本身；也可以改为更复杂的生成策略
    test_n = 10  # 可以修改为任意规模
    main(test_n)