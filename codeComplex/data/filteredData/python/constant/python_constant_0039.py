import random

def luck(n):
    if n % 4 == 0 or n % 7 == 0:
        return True
    while n > 0:
        tmp = n % 10
        n = n // 10
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

def main(n):
    # 根据规模 n 生成测试数据，这里生成 [1, 10^n] 范围内的随机数
    if n <= 0:
        test_value = 1
    else:
        upper = 10 ** n
        test_value = random.randint(1, upper)
    print(lucky(test_value))