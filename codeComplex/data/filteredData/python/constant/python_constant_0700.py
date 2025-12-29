import random

def main(n: int):
    # 根据规模 n 生成一组 (n, k) 测试数据
    # 假设 k 在 [0, n] 范围内随机生成
    k = random.randint(0, n) if n > 0 else 0

    # 原逻辑
    if k >= n - 1:
        result = n - 1
    else:
        result = k + ((n - k) * (n - k + 1)) // 2 - 1

    # 按原程序行为，仅打印结果
    print(result)


if __name__ == "__main__":
    # 示例：调用 main，规模可根据需要修改
    main(10)