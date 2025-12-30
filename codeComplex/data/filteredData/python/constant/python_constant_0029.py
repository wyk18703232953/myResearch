import random

def main(n: int):
    # 生成测试数据，这里直接使用传入的 n 作为原题中的输入
    # 原题逻辑：给定 n，输出 int(3 * n / 2)
    # 若想批量测试，可在此处生成多个随机 n 调用同一逻辑
    result = int(3 * n / 2)
    print(result)


if __name__ == "__main__":
    # 示例：根据需求自行设置规模 n 或测试多组数据
    # 这里给一个示例调用
    test_n = 10  # 示例规模，可按需修改或在外部调用 main(n)
    main(test_n)