from math import sqrt

def main(n):
    k = n * (n + 1) // 4
    a = 1
    b = -1 * (2 * n + 3)
    c = n * (n + 1) - 2 * k
    res = (-1 * b) - sqrt((b * b) - 4 * a * c)
    res = res / 2
    res = int(res)
    return res

if __name__ == "__main__":
    print(main(10))