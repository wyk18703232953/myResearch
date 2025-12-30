import random

def main(n: int):
    # 根据规模 n 生成测试数据：长度为 n 的随机整数数组 A
    # 这里生成范围在 [-10, 10] 之间的整数，可按需要调整
    A = [random.randint(-10, 10) for _ in range(n)]

    # 输出生成的测试数据（如果不需要可以删除这一行）
    print("A:", A)

    # 前缀和数组
    prefix = [0] * n
    prefix[0] = A[0]
    for i in range(1, n):
        prefix[i] = prefix[i - 1] + A[i]

    # 二分查找目标值
    target = (sum(A) + 1) // 2

    for i in range(n):
        if prefix[i] < target:
            continue
        else:
            print(i + 1)
            break


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)