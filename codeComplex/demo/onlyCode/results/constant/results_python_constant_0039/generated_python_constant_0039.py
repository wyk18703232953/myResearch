import random

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

def main(n):
    # 根据规模 n 生成一个 1 到 n 之间的随机测试数据
    test_value = random.randint(1, max(1, n))
    print(lucky(test_value))

if __name__ == "__main__":
    # 示例：使用 n = 100 作为规模
    main(100)