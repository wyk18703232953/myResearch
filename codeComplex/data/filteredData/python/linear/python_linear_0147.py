import random

def main(n):
    # 生成测试数据：n 和 p 以及数组 a
    # 这里示例设定 p 为一个较大的整数，且确保 p > 0
    p = random.randint(1, 10**9)
    a = [random.randint(-10**6, 10**6) for _ in range(n)]

    # 原始逻辑
    forward = [a[0]]
    for i in range(1, n):
        forward.append(forward[-1] + a[i])

    sm = sum(a)
    mx = -float('inf')
    for i in range(n - 1):
        mx = max(mx, (forward[i] % p) + ((sm - forward[i]) % p))

    print(mx)

# 示例调用
if __name__ == "__main__":
    main(5)