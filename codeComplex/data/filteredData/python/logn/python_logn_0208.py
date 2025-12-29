import random

def main(n):
    # 随机生成 s，保证 0 <= s <= n
    # 为了更有意义，s 尽量取在 [0, n] 内的随机值
    s = random.randint(0, n)

    lo = 0
    hi = n
    ans = n + 1

    while lo <= hi:
        mi = (lo + hi) >> 1
        curr = sum(int(i) for i in str(mi))
        if mi - curr >= s:
            hi = mi - 1
            ans = mi
        else:
            lo = mi + 1

    print(n - ans + 1)

if __name__ == "__main__":
    # 示例：可修改 n 的值进行测试
    main(10**9)