from random import randint

def main(n: int):
    # 根据规模 n 生成 l, r（保证 l <= r）
    # 这里示例设定比特长度为 n，数值范围在 [0, 2^n - 1]
    if n <= 0:
        l, r = 0, 0
    else:
        max_val = (1 << n) - 1
        l = randint(0, max_val)
        r = randint(l, max_val)

    # 原逻辑开始（单组 t=1）
    if len(bin(l)) < len(bin(r)):
        ans = (1 << len(bin(r)[2:])) - 1
    else:
        p = bin(l)[2:]
        q = bin(r)[2:]
        diff_len = 0
        for i in range(len(q)):
            if p[i] != q[i]:
                diff_len = len(p) - i
                break
        ans = (1 << diff_len) - 1

    print(ans)


if __name__ == "__main__":
    # 示例：n=5，可根据需要修改或在外部调用 main(n)
    main(5)