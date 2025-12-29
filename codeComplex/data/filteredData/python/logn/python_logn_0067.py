import random

def main(n):
    # 生成测试数据：根据规模 n 生成一个范围 [0, 2^n - 1] 内的随机区间 [l, r]
    if n <= 0:
        return
    l = random.randint(0, (1 << n) - 1)
    r = random.randint(l, (1 << n) - 1)

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
    # 示例：规模为 10
    main(10)