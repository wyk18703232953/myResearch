import random

def main(n):
    # 根据规模 n 生成测试数据，这里直接将 n 作为测试数据使用
    # 若需要更复杂的生成逻辑，可在此根据 n 构造不同的测试用例
    result = n**2 + (n - 1)**2
    print(result)

if __name__ == "__main__":
    # 示例：可在此修改 n 以进行测试
    main(10)