import random

def main(n):
    # 生成测试数据
    # k 范围可根据需要调整，这里取 1 ~ n 之间
    k = random.randint(1, max(1, n))
    # 数组 a 中元素范围可调整，这里简单取 1 ~ 10*n
    a = [random.randint(1, 10 * n) for _ in range(n)]

    # 原逻辑开始
    a.sort()
    j = 0
    n1 = n
    for i in range(n):
        while j < n and a[j] < a[i]:
            if a[i] <= a[j] + k:
                n1 -= 1
            j += 1
            if j >= n:  # 防止越界
                break
    print(n1)

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)