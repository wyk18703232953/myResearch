import math
import random

def main(n):
    # n 为规模参数，用于控制随机测试数据生成范围
    # 这里生成 6 个非负整数，范围与 n 相关，可按需要调整
    # 保证不全为 0，便于产生有意义的测试
    while True:
        xy = [random.randint(0, n) for _ in range(6)]
        if any(xy):
            break

    x = [[xy[0], xy[2], xy[4]], [xy[1], xy[3], xy[5]]]
    aa = 0
    max_ll = 0
    for i in range(3):
        aa += x[0][i] * x[1][i]
        max_ll = max(max_ll, x[0][i], x[1][i])

    bb = math.isqrt(aa)
    if bb * bb != aa or max_ll != bb:
        print(-1)
        return

    bb = int(bb)
    mt = [[''] * bb for _ in range(bb)]
    max_l = 0
    chars = ['A', 'B', 'C']
    x = [[xy[0], xy[1]], [xy[2], xy[3]], [xy[4], xy[5]]]
    max_lp = -1
    max_li = -1
    ii = 0
    oh = []
    for i in x:
        if max(i) >= max_l:
            max_l = max(i)
            max_lp = sum(i) - max(i)
            max_li = ii
        ii += 1

    max_ls = []
    ii = 0
    for i in x:
        if max(i) == max_l:
            max_ls.append(i + [ii])
        else:
            oh.append(ii)
        ii += 1

    if len(max_ls) == 3:
        for i in range(max_l):
            for j in range(max_l):
                if i < (max_ls[0][0] + max_ls[0][1] - max_l):
                    mt[i][j] = chars[max_ls[0][2]]
                elif i < (max_ls[0][0] + max_ls[0][1] - max_l +
                          max_ls[1][0] + max_ls[1][1] - max_l):
                    mt[i][j] = chars[max_ls[1][2]]
                else:
                    mt[i][j] = chars[max_ls[2][2]]
    else:
        for i in range(max_lp):
            for j in range(max_l):
                mt[i][j] = chars[max_li]

        bb2 = max_l - max_lp
        for i in range(max_lp, max_l):
            for j in range(max_l):
                if j < (sum(x[oh[0]]) - bb2):
                    mt[i][j] = chars[oh[0]]
                else:
                    mt[i][j] = chars[oh[1]]

    print(max_l)
    for row in mt:
        print(''.join(row))


if __name__ == "__main__":
    # 示例：n = 10，可根据需要修改
    main(10)