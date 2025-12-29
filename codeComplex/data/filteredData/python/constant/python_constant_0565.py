import random

def main(n):
    # 生成测试数据：
    # 约定：
    # 1 <= m <= n
    # 0 <= k, l <= n
    if n <= 0:
        return -1

    m = random.randint(1, n)
    k = random.randint(0, n)
    l = random.randint(0, n)

    # 原逻辑
    if m > n:
        return -1
    elif l + k > n:
        return -1
    else:
        s = (l + k) // m + bool((l + k) % m)
        if s * m > n:
            return -1
        else:
            return s

if __name__ == "__main__":
    # 示例：固定 n 来运行
    n = 10
    ans = main(n)
    print(ans)