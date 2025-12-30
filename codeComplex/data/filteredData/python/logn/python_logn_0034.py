import random

def main(n: int):
    # 生成测试数据：在 [0, 2^n - 1] 范围内随机生成 l, r
    if n <= 0:
        return
    max_val = (1 << n) - 1
    l = random.randint(0, max_val)
    r = random.randint(0, max_val)
    # 保证 l <= r，逻辑与原题一致（原题默认输入为一行 l r）
    if l > r:
        l, r = r, l

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


if __name__ == "__main__":
    # 示例：传入规模 n，例如 10
    main(10)