import random

def main(n: int):
    # 根据规模 n 生成测试数据
    # 这里假设 n 表示 l、r 的最大可能值
    # 随机生成 0 <= l <= r <= n
    l = random.randint(0, n)
    r = random.randint(l, n)

    # 原逻辑
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
    # 示例调用，可根据需要修改 n 的值
    main(10**6)