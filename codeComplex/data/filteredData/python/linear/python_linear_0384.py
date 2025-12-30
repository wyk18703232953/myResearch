import random

def main(n):
    # 生成测试数据：m 条记录，每条为 [a0, a1]
    # 可根据需要调整 m 和系数范围
    m = max(1, n)  # 简单设为 m = n（至少为 1）
    arr = []
    for _ in range(m):
        a0 = random.randint(-10, 10)
        a1 = random.randint(-10, 10)
        arr.append([a0, a1])

    count = 0
    for i in range(m):
        count += arr[i][0] * n
        if n % 2 == 1 and arr[i][1] < 0:
            count += (n // 2) * (n // 2 + 1) * arr[i][1]
        if n % 2 == 1 and arr[i][1] > 0:
            count += n * (n - 1) * arr[i][1] // 2
        if n % 2 == 0 and arr[i][1] < 0:
            count += (n // 2) * (n // 2 - 1) * arr[i][1]
            count += (n // 2) * arr[i][1]
        if n % 2 == 0 and arr[i][1] > 0:
            count += n * (n - 1) * arr[i][1] // 2

    print(count / n)


if __name__ == "__main__":
    # 示例调用
    main(5)