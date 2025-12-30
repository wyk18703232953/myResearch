import random

def main(n: int):
    # 根据 n 生成测试数据，这里简单地覆盖输入为 n 本身
    # 也可以扩展为随机测试列表等
    if n % 2 == 0:
        print(f"4 {n - 4}")
    else:
        print(f"9 {n - 9}")


if __name__ == "__main__":
    # 示例：可在此处修改 n 进行测试
    test_n = 20  # 这里作为示例规模
    main(test_n)