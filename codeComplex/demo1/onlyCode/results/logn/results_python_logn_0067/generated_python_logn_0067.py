import random

def main(n: int):
    # 生成测试数据：根据规模 n 生成 l, r
    # 这里令 l, r 在 [0, 2^n - 1] 范围内，且保证 l <= r
    if n <= 0:
        l, r = 0, 0
    else:
        upper = (1 << n) - 1
        l = random.randint(0, upper)
        r = random.randint(l, upper)

    # 以下为原始逻辑（去除 input() 并封装）
    p = l
    lp = -1
    while p:
        p = p >> 1
        lp += 1

    q = r
    rp = -1
    while q:
        q = q >> 1
        rp += 1

    s = max(lp, rp)

    ans = 0

    while s >= 0:
        if (l >> s) & 1 != (r >> s) & 1:
            ans |= ((r >> s) & 1) << s
            break
        s -= 1

    s -= 1

    while s >= 0:
        ans |= 1 << s
        s -= 1

    print(ans)

if __name__ == "__main__":
    # 示例：使用 n = 10 作为规模运行
    main(10)