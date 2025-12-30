import random

def main(n: int):
    # 生成规模为 n 的测试数据
    # 这里假设 m 为 n 的一半（可按需调整规则）
    m = max(1, n // 2)

    # 生成升序数组 arr1 和 arr2，元素值在 1 到 10*n 之间
    arr1 = sorted(random.randint(1, 10 * n) for _ in range(n))
    arr2 = sorted(random.randint(1, 10 * n) for _ in range(m))

    j = 0
    for i in range(n):
        if j < m and arr2[j] >= arr1[i]:
            j += 1
    print(j)


if __name__ == "__main__":
    # 示例：运行规模为 10 的测试
    main(10)