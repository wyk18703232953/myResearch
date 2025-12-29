import random

def main(n):
    # 生成测试数据：n 和数组 a（长度为 n，元素为非负整数）
    # 这里示例取 a[i] 在 [0, 10] 内，可按需要自行调整
    m = n  # 原代码中读入了 m，但未使用，这里保持形式一致
    a = [random.randint(0, 10) for _ in range(n)]

    a.sort()
    last = 0
    total = 0
    for i in range(n - 1):
        if a[i] > 0:
            total += a[i] - 1
            last = min(last + 1, a[i])

    ans = total + max(a[n - 1] - max(1, a[n - 1] - last), 0)
    print(ans)


if __name__ == "__main__":
    # 示例调用：n = 10
    main(10)