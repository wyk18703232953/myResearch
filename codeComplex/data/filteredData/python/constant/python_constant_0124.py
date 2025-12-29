import random

def main(n: int):
    # 这里的 n 表示要生成的测试数据的数量
    for _ in range(n):
        # 生成测试数据：范围可根据需要调整，这里示例为 [-10^9, 10^9]
        x = random.randint(-10**9, 10**9)
        result = transform_number(x)
        print(result)

def transform_number(n: int) -> int:
    # 原逻辑的函数化实现
    if n >= 0:
        return n
    else:
        n_abs = abs(n)
        rem = n_abs % 10
        n1 = n_abs // 10
        n2 = n1 // 10
        n2 = n2 * 10 + rem
        k = min(n1, n2)
        return -1 * k

if __name__ == "__main__":
    # 示例：生成 5 组测试数据并输出结果
    main(5)