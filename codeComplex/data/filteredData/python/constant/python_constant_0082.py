import random

def Solve(n):
    if n <= 2:
        return n
    elif n % 6 == 0:
        return (n - 1) * (n - 2) * (n - 3)
    elif n % 2 == 0:
        return n * (n - 1) * (n - 3)
    else:
        return n * (n - 1) * (n - 2)

def main(n):
    # 生成规模为 n 的测试数据：这里直接使用 n 作为待求解参数
    # 如需更复杂测试数据，可在此处扩展生成逻辑
    test_n = n
    result = Solve(test_n)
    print(result)

if __name__ == "__main__":
    # 示例：可修改为任意正整数规模
    main(10)