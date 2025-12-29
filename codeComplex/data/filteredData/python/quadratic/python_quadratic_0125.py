import random

def main(n: int):
    # 生成测试数据：m 在 [0, n] 内，A 为长度为 m、元素在 [1, n] 的数组
    m = random.randint(0, n)
    A = [random.randint(1, n) for _ in range(m)]

    L = [0] * n
    for i in range(m):
        L[A[i] - 1] += 1
    print(min(L))


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    main(10)