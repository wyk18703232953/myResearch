import random

def req_factory(tar1, tar2):
    # 构造一个本地的 req 函数，模拟交互返回值
    def req(a, b, c, d):
        ans = 0
        for t in (tar1, tar2):
            if a <= t[0] and b <= t[1] and c >= t[2] and d >= t[3]:
                ans += 1
        return ans
    return req


def bin_search(l, r, down, left, up, right, tp, tar, req):
    while r - l > 1:
        m = (r + l) // 2

        d2, l2, u2, r2 = down, left, up, right
        if tp == 0:
            d2 = m
        elif tp == 1:
            l2 = m
        elif tp == 2:
            u2 = m
        else:  # tp == 3
            r2 = m

        if req(d2, l2, u2, r2) == tar:
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


def gen_random_rectangle(n):
    x1 = random.randint(1, n)
    x2 = random.randint(x1, n)
    y1 = random.randint(1, n)
    y2 = random.randint(y1, n)
    return [x1, y1, x2, y2]


def main(n):
    # 生成两个随机矩形作为测试数据
    tar1 = gen_random_rectangle(n)
    tar2 = gen_random_rectangle(n)

    # 绑定 req
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

    # 输出找到的两个矩形以及真实矩形，便于验证
    print("found:", *rec[0], *rec[1])
    print("actual:", *tar1, *tar2)


# 示例调用
if __name__ == "__main__":
    main(10)