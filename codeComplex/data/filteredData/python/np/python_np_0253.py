import math

def main(n):
    # n controls the magnitude of the 6 integers: they will be in [1, max(1, n)]
    m = max(1, n)
    xy = [
        (i % m) + 1
        for i in range(6)
    ]

    x = [[xy[0], xy[2], xy[4]], [xy[1], xy[3], xy[5]]]
    aa = 0
    max_ll = 0
    for i in range(3):
        aa += x[0][i] * x[1][i]
        max_ll = max(max_ll, x[0][i], x[1][i])

    bb = math.sqrt(aa)
    if bb * bb != aa or max_ll != bb:
        print(-1)
        return
    else:
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

            bb = max_l - max_lp
            for i in range(max_lp, max_l):
                for j in range(max_l):
                    if j < (sum(x[oh[0]]) - bb):
                        mt[i][j] = chars[oh[0]]
                    else:
                        mt[i][j] = chars[oh[1]]

        print(max_l)
        for row in mt:
            print(''.join(row))


if __name__ == "__main__":
    main(10)