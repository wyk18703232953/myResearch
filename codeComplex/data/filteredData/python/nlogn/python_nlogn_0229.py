import random

def gcd(a, b):
    if a > b:
        a, b = b, a
    if b % a == 0:
        return a
    return gcd(b % a, a)

def line(a, b):
    x0, y0 = a
    x1, y1 = b
    if x0 == x1:
        return [True, x1, None]
    else:
        slope_num = (y1 - y0)
        slope_den = (x1 - x0)
        if slope_num == 0:
            num = 0
            den = 1
        else:
            g = gcd(abs(slope_num), abs(slope_den))
            num = slope_num // g
            den = slope_den // g
        inter = den * y0 - num * x0
        if inter == 0:
            den2 = 1
        else:
            den2 = den
        return [False, num, den, inter, den2]

def online(l, a):
    x0, y0 = a
    if l[0]:
        return x0 == l[1]
    else:
        C, num, den, inter, den2 = l
        return (num * x0 + inter) == y0 * den

def process(A):
    n = len(A)
    if n <= 3:
        return 'YES'
    l1 = line(A[0], A[1])
    l2 = line(A[1], A[2])
    l3 = line(A[0], A[2])
    for Line1 in [l1, l2, l3]:
        other = []
        for x in A:
            if not online(Line1, x):
                other.append(x)
        if len(other) <= 2:
            return 'YES'
        a1 = other[0]
        a2 = other[1]
        Line2 = line(a1, a2)
        works = True
        for x in other:
            if not online(Line2, x):
                works = False
                break
        if works:
            return 'YES'
    return 'NO'

def generate_test_data(n):
    # 生成 n 个点，坐标范围可根据需要调整
    A = []
    for _ in range(n):
        x = random.randint(-10**6, 10**6)
        y = random.randint(-10**6, 10**6)
        A.append([x, y])
    return A

def main(n):
    A = generate_test_data(n)
    result = process(A)
    print(result)

if __name__ == "__main__":
    # 示例：调用 main(10)。实际使用时，可修改 n。
    main(10)