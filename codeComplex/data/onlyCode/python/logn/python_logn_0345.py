modulo = 1000 ** 3 + 7


def mat_oz(x, k):
    if k == 0:
        return (2 * x) % modulo
    if x == 0:
        return 0
    b = (pow(2, k, modulo) * (2 * x - 1) + 1) % modulo
    return b


y, m = [int(i) for i in input().split()]
print(mat_oz(y, m))
