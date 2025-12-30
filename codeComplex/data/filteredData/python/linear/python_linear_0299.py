import random

def main(n: int):
    # 根据 n 生成测试数据：随机生成 n 个整数，范围可按需调整
    # 这里选择 [-10, 10] 范围，方便包含或不包含 0 的情况
    data = [random.randint(-10, 10) for _ in range(n)]

    arr = set(data)
    result = len(arr) - (0 in arr)
    print(result)

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)