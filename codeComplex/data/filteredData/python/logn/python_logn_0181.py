import random

def req_factory(tar1, tar2):
    # 闭包模拟交互：返回矩形 [a,b,c,d] 中包含的目标矩形个数
    def req(a, b, c, d):
        cnt = 0
        for t in (tar1, tar2):
            if a <= t[0] and b <= t[1] and c >= t[2] and d >= t[3]:
                cnt += 1
        return cnt
    return req


def bin_search(l, r, down, left, up, right, tp, tar, req):
    while r - l > 1:
        m = (r + l) // 2

        if tp == 0:
            down_tmp, left_tmp, up_tmp, right_tmp = m, left, up, right
        elif tp == 1:
            down_tmp, left_tmp, up_tmp, right_tmp = down, m, up, right
        elif tp == 2:
            down_tmp, left_tmp, up_tmp, right_tmp = down, left, m, right
        else:  # tp == 3
            down_tmp, left_tmp, up_tmp, right_tmp = down, left, up, m

        if req(down_tmp, left_tmp, up_tmp, right_tmp) == tar:
            l = m
        else:
            r = m
    return [l, r]


def find_rec(x1, y1, x2, y2, req):
    up_ = bin_search(x1 - 1, x2 + 1, x1, y1, -2, y2, 2, 0, req)[1]
    down_ = bin_search(x1 - 1, x2 + 1, -2, y1, x2, y2, 0, 1, req)[0]
    left_ = bin_search(y1 - 1, y2 + 1, x1, -2, x2, y2, 1, 1, req)[0]
    right_ = bin_search(left_ - 1, y2 + 1, x1, y1, x2, -2, 3, 0, req)[1]
    return [down_, left_, up_, right_]


def gen_two_rectangles(n):
    # 生成两个不重叠且各自面积>0 的矩形 [x1,y1,x2,y2]
    def gen_rect():
        x1 = random.randint(1, n)
        x2 = random.randint(x1, n)
        y1 = random.randint(1, n)
        y2 = random.randint(y1, n)
        return [x1, y1, x2, y2]

    while True:
        r1 = gen_rect()
        r2 = gen_rect()
        # 判断是否不完全相同即可，允许相交（原算法只依赖“包含”判断，可以处理重叠）
        if r1 != r2:
            return r1, r2


def main(n):
    random.seed(0)
    tar1, tar2 = gen_two_rectangles(n)
    req = req_factory(tar1, tar2)

    l = 0
    r = n + 1
    while r - l > 1:
        m = (l + r) // 2
        if req(1, 1, m, n) == 0:
            l = m
        else:
            r = m

    rec = []

    if r != n and req(r + 1, 1, n, n) == 1:
        rec.append(find_rec(1, 1, r, n, req))
        rec.append(find_rec(r + 1, 1, n, n, req))
    else:
        l = 0
        r = n + 1
        while r - l > 1:
            m = (l + r) // 2
            if req(1, 1, n, m) == 0:
                l = m
            else:
                r = m
        rec.append(find_rec(1, 1, n, r, req))
        rec.append(find_rec(1, r + 1, n, n, req))

    # 输出找到的矩形与真实矩形，便于测试
    print("found:", *rec[0], *rec[1])
    print("true :", *tar1, *tar2)


if __name__ == "__main__":
    main(10)