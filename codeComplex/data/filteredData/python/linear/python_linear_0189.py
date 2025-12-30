import random

def main(n: int):
    # 1. 生成测试数据：长度为 n 的随机整数数组
    # 这里生成 1 到 100 之间的随机数，可按需调整范围
    a = [random.randint(1, 100) for _ in range(n)]

    # 2. 原逻辑
    s = sum(a)
    new = 0
    i = 0
    # 注意避免越界，如果 n 很小或条件不满足要检查 i < n
    while i < n and 2 * (new + a[i]) < s:
        new += a[i]
        i += 1

    # 当循环自然结束，若 i == n，表示整个数组都不满足条件
    # 根据原算法语义，此时 i+1 可能超出原范围，但仍照搬原打印逻辑
    print(i + 1)

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)