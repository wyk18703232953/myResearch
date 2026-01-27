one = list(map(int, input().split()))
two = list(map(int, input().split()))

one_ = sorted([(one[i], one[i + 1]) for i in range(0, 8, 2)], key=lambda x: (x[1], x[0]))
two_ = sorted([(two[i], two[i + 1]) for i in range(0, 8, 2)], key=lambda x: (x[1], x[0]))

ones = [one_[0], one_[2], one_[3], one_[1]]
twos = [two_[1], two_[3], two_[2], two_[0]]

L, D, U, R = ones[0][0], ones[0][1], ones[2][1], ones[2][0]


def in_one(point):
    x, y = point

    return L <= x <= R and D <= y <= U


def in_two(point):
    x_0, y_0 = twos[0]

    def U_p(x_):
        return x_ + y_0 - x_0

    def D_m(x_):
        return -x_ + y_0 + x_0

    x_1, y_1 = twos[2]

    def U_m(x_):
        return -x_ + y_1 + x_1

    def D_p(x_):
        return x_ + y_1 - x_1

    x, y = point
    
    return D_m(x) <= y <= U_p(x) and D_p(x) <= y <= U_m(x)


c_one = ((L + R) / 2, (U + D) / 2)
c_two = ((twos[0][0] + twos[2][0]) / 2, (twos[1][1] + twos[3][1]) / 2)

ones.append(c_one)
twos.append(c_two)

for p in ones:
    if in_two(p):
        print('YES')
        exit()

for p in twos:
    if in_one(p):
        print('YES')
        exit()

print('NO')
