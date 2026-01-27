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
    # 将规模 n 映射为原程序的单个整数输入
    # 这里选择输入值为 n 本身（保证确定性且可扩展）
    value = n
    result = lucky(value)
    # print(result)
    pass
if __name__ == "__main__":
    main(100)