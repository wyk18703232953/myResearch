import random

def po(a, p, m):
    if p == 0:
        return 1
    x = po(a, p // 2, m) % m
    x = (x * x) % m
    if p % 2 == 1:
        x = (x * a) % m
    return int(x)

def main(n):
    """
    n 作为规模参数，用于生成测试数据:
    - x: 1 到 n 之间的随机整数
    - k: 0 到 n 之间的随机整数
    输出与原程序等价的结果。
    """
    m = 1000000007

    # 根据 n 生成测试数据
    if n <= 0:
        x = 0
        k = 0
    else:
        x = random.randint(0, n)   # 允许生成 0，以覆盖 x==0 分支
        k = random.randint(0, n)

    if x == 0:
        print(0)
    else:
        res = ((po(2, k + 1, m) * x) % m - (po(2, k, m) - 1) % m) % m
        print(res)

if __name__ == "__main__":
    # 示例：使用规模 n=10 运行
    main(10)