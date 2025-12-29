import random

def main(n):
    # 根据 n 生成测试数据（示例：生成一个长度为 n 的随机数组）
    # 实际使用中可根据需求替换为合适的数据生成逻辑
    test_data = [random.randint(0, 100) for _ in range(n)]
    
    # 原始逻辑：输出 '0', '0', n
    # 为保持原逻辑，同时展示生成的数据，这里仍然按原要求输出三项，
    # 若只需这三项，可忽略 test_data
    print('0', '0', n)

    # 如需查看生成的测试数据，可取消注释下面一行
    # print(test_data)


if __name__ == "__main__":
    # 示例：调用 main(10)，实际使用时由外部指定 n
    main(10)