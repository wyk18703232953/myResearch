import random

def main(n: int):
    # 根据 n 生成测试数据（此处示例：生成一个长度为 n 的随机整数数组）
    test_data = [random.randint(0, 100) for _ in range(n)]
    
    # 保留原始程序的核心输出逻辑（这里原始逻辑只与 n 有关，与 test_data 无关）
    print(0, 0, n)

    # 如需查看生成的测试数据，可取消下一行注释
    # print(test_data)


if __name__ == "__main__":
    # 示例：调用 main，规模 n 自行设定
    main(10)