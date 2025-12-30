import random

def main(n):
    # 1. 生成测试数据：在一定范围内随机生成 l, r
    # 为了让规模 n 起作用，这里用 n 控制上界：0 <= l, r <= 2^n - 1
    if n <= 0:
        # 规模太小则给出固定小例子
        l, r = 8, 20
    else:
        upper = (1 << n) - 1
        l = random.randint(0, upper)
        r = random.randint(0, upper)
        if l > r:
            l, r = r, l  # 保证 l <= r

    # 原始逻辑：计算区间 [l, r] 内任意两个数的最大异或值
    q = l ^ r
    a = 1
    while q:
        q //= 2
        a <<= 1

    result = a - 1
    print(result)


if __name__ == "__main__":
    # 示例：可根据需要修改 n
    main(10)