# tar1 = [3, 4, 10, 4]
# tar2 = [1, 1, 10, 1]


def req(a, b, c, d):
    # if 11 in [a, b, c, d]:
    #     print('here')
    # ans = 0
    # for i in [tar1, tar2]:
    #     if a <= i[0] and b <= i[1] and c >= i[2] and d >= i[3]:
    #         ans += 1
    # return ans
    print(f"? {a} {b} {c} {d}")
    return int(input())


def bin(l, r, down, left, up, right, tp, tar):
    while r - l > 1:
        m = (r + l) // 2

        if tp == 0:
            down = m
        if tp == 1:
            left = m
        if tp == 2:
            up = m
        if tp == 3:
            right = m

        if req(down, left, up, right) == tar:
            l = m
        else:
            r = m
    return [l, r]


def find_rec(x1, y1, x2, y2) -> list:
    up_ = bin(x1 - 1, x2 + 1, x1, y1, -2, y2, 2, 0)[1]
    down_ = bin(x1 - 1, x2 + 1, -2, y1, x2, y2, 0, 1)[0]
    left_ = bin(y1 - 1, y2 + 1, x1, -2, x2, y2, 1, 1)[0]
    right_ = bin(left_ - 1, y2 + 1, x1, y1, x2, -2, 3, 0)[1]
    return [down_, left_, up_, right_]


n = int(input())
# n = 10

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
    rec.append(find_rec(1, 1, r, n))
    rec.append(find_rec(r + 1, 1, n, n))
else:
    l = 0
    r = n + 1
    while r - l > 1:
        m = (l + r) // 2
        if req(1, 1, n, m) == 0:
            l = m
        else:
            r = m
    rec.append(find_rec(1, 1, n, r))
    rec.append(find_rec(1, r + 1, n, n))
print('!', *rec[0], *rec[1])
