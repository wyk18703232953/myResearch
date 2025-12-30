import random

def main(n):
    """
    n: 规模参数，用来控制测试数据范围。
    程序会自动生成 n, m, k, l 四个参数，其中：
      1 <= m <= max(1, n)
      0 <= k, l <= n
    然后执行原逻辑并打印结果。
    """
    if n <= 0:
        # 对于非正规模，给出一个固定用例
        N = 10
        m = 3
        k = 2
        l = 5
    else:
        # 生成测试数据
        N = n
        m = random.randint(1, max(1, n))
        k = random.randint(0, N)
        l = random.randint(0, N)

    # 原逻辑开始
    d = (l + k) // m
    if (l + k) % m:
        d += 1
    if m * d > N or N - k < l:
        print(-1)
    else:
        print(d)


if __name__ == "__main__":
    # 示例：调用 main，规模设置为 100
    main(100)