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


a, b = [int(i) for i in input().split()]
print(result(a, b))
