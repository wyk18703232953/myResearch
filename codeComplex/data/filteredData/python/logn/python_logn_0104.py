import random

def main(n: int):
    # 生成测试数据：根据规模 n 生成 l, r
    # 这里约定：0 <= l <= r < 2^n
    if n <= 0:
        l, r = 0, 0
    else:
        upper = 1 << n
        l = random.randrange(0, upper)
        r = random.randrange(0, upper)
        if l > r:
            l, r = r, l

    # 原逻辑开始
    lxr = l ^ r
    msb = 0
    while lxr:
        msb += 1
        lxr >>= 1
    m = 0
    t = 1
    while msb:
        m += t
        t <<= 1
        msb -= 1

    print(m)


if __name__ == "__main__":
    # 示例：可自行修改 n 测试
    main(10)