from math import factorial

def C(m, n):
    return factorial(n) // (factorial(m) * factorial(n - m))

def main(n):
    # 构造确定性的 command_1 和 command_2
    # 令 command_1 的长度为 n，依次交替 '+' 和 '-'
    command_1 = ''.join('+' if i % 2 == 0 else '-' for i in range(n))
    # 令 command_2 的长度为 n，前 n//3 为 '+'，中间 n//3 为 '-'，剩余为 '?'
    part1 = n // 3
    part2 = n // 3
    part3 = n - part1 - part2
    command_2 = '+' * part1 + '-' * part2 + '?' * part3

    num = command_2.count('?')
    i = (command_1.count('+') - command_1.count('-')
         - command_2.count('+') + command_2.count('-') + num)
    if i % 2 == 0 and 0 <= i // 2 <= num:
        print("%.9f" % (C(i // 2, num) / 2 ** num))
    else:
        print("0.000000000")

if __name__ == "__main__":
    main(10)