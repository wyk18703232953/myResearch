import random


def main(n: int):
    # 生成测试数据：
    # 原程序中 a,b,c,d,e,f 是任意非负整数（通常题目会有合理范围限制）
    # 这里根据规模 n 生成，使得总面积接近 n^2
    # 生成 3 对边长 (a,b), (c,d), (e,f)，再稍微调节使 a*b + c*d + e*f == n^2 尽量经常成立

    def gen_rect():
        # 随机生成一对边长，范围与 n 同级
        x = random.randint(1, n)
        y = random.randint(1, n)
        return x, y

    # 初始随机生成
    a, b = gen_rect()
    c, d = gen_rect()
    e, f = gen_rect()

    total_area = a * b + c * d + e * f

    # 简单的调整策略：尝试修改 f 以让总面积接近 n^2
    # total_area' = a*b + c*d + e*f' == n^2  =>  f' = (n^2 - a*b - c*d)/e
    # 若能得到正整数 f'，就使用；否则保留随机值，让程序可能输出 -1
    base = a * b + c * d
    if e != 0:
        remain = n * n - base
        if remain > 0 and remain % e == 0:
            f_candidate = remain // e
            if 1 <= f_candidate <= 2 * n:
                f = f_candidate
                total_area = a * b + c * d + e * f

    # ===== 以下是原始逻辑，去掉 input()，使用生成好的 a,b,c,d,e,f =====

    n2 = a * b + c * d + e * f
    n_side = 1
    while n_side ** 2 < n2:
        n_side += 1
    if n_side ** 2 > n2:
        print(-1)
        return

    l = sorted([
        [max(a, b), min(a, b), 'A'],
        [max(c, d), min(c, d), 'B'],
        [max(e, f), min(e, f), 'C']
    ])

    if l[2][0] != n_side:
        print(-1)
        return

    v = str(n_side) + '\n' + (l[2][2] * n_side + '\n') * l[2][1]

    if l[0][0] == n_side and l[1][0] == n_side:
        for i in range(2):
            v += (l[i][2] * n_side + '\n') * l[i][1]
    else:
        s = n_side - l[2][1]
        if s not in l[0] or s not in l[1]:
            print(-1)
            return
        x = l[0][1] if l[0][0] == s else l[0][0]
        y = l[1][1] if l[1][0] == s else l[1][0]
        v += (l[0][2] * x + l[1][2] * y + '\n') * s

    print(v)


if __name__ == "__main__":
    # 示例：调用 main，规模 n 可自行调整
    main(10)