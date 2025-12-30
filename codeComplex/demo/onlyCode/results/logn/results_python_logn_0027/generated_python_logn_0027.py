import random

def main(n):
    """
    n 为规模参数，用于控制测试数据范围：
    这里设定 l, r 在 [0, 2^n - 1] 范围内随机生成，且保证 l <= r。
    """
    if n <= 0:
        # 退化情形，直接使用 0,0
        l = 0
        r = 0
    else:
        upper = (1 << n) - 1
        l = random.randint(0, upper)
        r = random.randint(0, upper)
        if l > r:
            l, r = r, l

    # 以下是原逻辑
    if l == r:
        print("0")
        return

    i = 0
    j = 0
    ll = l   # 为避免修改原值，若有需要保留可用 ll, rr 替代
    rr = r
    while ll > 0 or rr > 0:
        i += 1
        if (ll & 1) ^ (rr & 1) == 1:
            j = i
        ll = ll >> 1
        rr = rr >> 1

    ans = 1
    for _ in range(j):
        ans *= 2
    ans -= 1
    print(ans)


if __name__ == "__main__":
    # 示例：调用 main，n 可根据需要修改
    main(10)