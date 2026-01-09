M = 10**9 + 7

def solve(x, k):
    if x == 0:
        return 0
    return ((pow(2, k + 1, M) * x) % M - pow(2, k, M) + 1) % M

def main(n):
    """
    n 为规模参数，这里用于控制测试数据数量。
    生成 n 组 (x, k) 测试数据，并输出对应结果。
    测试数据示例策略：
      x = i
      k = i^2
    """
    results = []
    for i in int_range(1, n + 1):
        x = i
        k = i * i
        results.append(solve(x, k))
    # 统一输出，按行打印
    for ans in results:
        # print(ans)
        pass

def int_range(a, b):
    """兼容大范围简单整数迭代的辅助函数：生成 [a, b)"""
    while a < b:
        yield a
        a += 1

if __name__ == "__main__":
    # 示例：以 n = 5 运行
    main(5)