import random

def main(n):
    # 1. 生成测试数据
    # 约定：k 在 [1, n] 内随机生成，arr 为长度为 n 的整数数组
    if n <= 0:
        return 0

    k = random.randint(1, n)
    # 生成一个有序数组，保证原算法的语义（一般用于区间划分/差分）
    arr = sorted(random.randint(0, 1000) for _ in range(n))

    # 2. 原逻辑
    kek = [0] * (n - 1)
    for i in range(n - 1):
        kek[i] = -arr[i + 1] + arr[i]

    kek.sort()

    ans = arr[-1] - arr[0]
    for i in range(k - 1):
        ans += kek[i]

    print(ans)
    return 0

# 示例调用
if __name__ == "__main__":
    main(10)