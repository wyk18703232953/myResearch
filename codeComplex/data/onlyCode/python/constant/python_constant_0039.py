def luck(n):
    if n % 4 == 0 or n % 7 == 0:
        return True
    while n > 0:
        tmp = n % 10
        n = int(n / 10)
        if tmp != 4 and tmp != 7:
            return False

    return True


def lucky(n):
    if luck(n):
        return "YES"

    for x in range(1, n + 1):
        if n % x == 0 and luck(x):
            return "YES"

    return "NO"


n = int(input())

print(lucky(n))