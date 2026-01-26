import math

def get_digit(x, pos):
    s = []
    while x > 0:
        s.append(x % 10)
        x //= 10
    return s[::-1][pos]

def find_digit(x):
    n = 0
    next_ = 9 * (10 ** n) * (n + 1)
    while next_ <= x:
        x -= next_
        n += 1
        next_ = 9 * (10 ** n) * (n + 1)
    if x == 0:
        return 9
    pos_ = 10 ** n + math.ceil(x / (n + 1)) - 1
    return get_digit(pos_, (x - 1) % (n + 1))

def main(n):
    k = n
    res = find_digit(k)
    # print(res)
    pass
if __name__ == "__main__":
    main(10_000_000)