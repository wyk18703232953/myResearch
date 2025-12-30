import random

def main(n: int):
    # 根据规模 n 生成测试数据：随机生成两个整数 l, r，且 l <= r
    # 取值范围可与 n 相关，这里设为 [0, 2^n - 1]
    if n <= 0:
        return

    max_val = (1 << n) - 1
    l = random.randint(0, max_val)
    r = random.randint(0, max_val)
    if l > r:
        l, r = r, l

    # 原逻辑开始
    r_bin = bin(r)[2:]
    l_bin = bin(l)[2:]

    r_rev = r_bin[::-1]
    l_rev = l_bin[::-1]

    if l_rev == r_rev:
        print(0)
    else:
        l_rev += '0' * (len(r_rev) - len(l_rev))
        p = -1
        for i in range(len(r_rev)):
            if r_rev[i] != l_rev[i]:
                p = i

        a = '1' * p + '0'
        b = '0' * p + '1'

        print(int(a, 2) ^ int(b, 2))


if __name__ == "__main__":
    # 示例：规模设为 10，可自行修改
    main(10)