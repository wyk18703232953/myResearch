def summing(number):
    summa = 0
    while number > 0:
        summa += number % 10
        number = number // 10
    return summa


def result(n, s):
    z = min(s, n)
    while z <= n and z - summing(z) < s:
        z += 1
    return n - z + 1


def main(n):
    a = n
    s = n // 2
    res = result(a, s)
    # print(res)
    pass
if __name__ == "__main__":
    main(10)