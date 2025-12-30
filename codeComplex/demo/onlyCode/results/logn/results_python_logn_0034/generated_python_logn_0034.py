import random

def main(n: int):
    # 1. 生成规模为 n 的测试数据：两个非负整数 l, r
    # 为了使规模有意义，用 n 控制数值大小范围 [0, 2^n - 1]
    if n <= 0:
        # 退化情况，给定一个固定样例
        l, r = 0, 1
    else:
        max_val = (1 << n) - 1
        l = random.randint(0, max_val)
        r = random.randint(0, max_val)
        # 保证 l <= r，和原题语义一致（不强制要求也可以）
        if l > r:
            l, r = r, l

    # 2. 原逻辑开始
    if l == r:
        print(0)
        return

    l_bin = bin(l)[2:].zfill(64)
    r_bin = bin(r)[2:].zfill(64)

    i = 0
    while i < len(r_bin):
        if l_bin[i] == r_bin[i]:
            i += 1
        else:
            break

    rslt = len(r_bin[:i]) * '0' + len(r_bin[i:]) * '1'
    print(int(rslt, 2))


# 示例：直接调用 main(10) 进行一次运行
if __name__ == "__main__":
    main(10)