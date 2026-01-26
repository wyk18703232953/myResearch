import math

def main(n):
    if n <= 0:
        print("0.000000000000")
        return

    # 确定性构造 str1 和 str2
    # str1: 前半部分 '+', 后半部分 '-'
    half = n // 2
    str1 = ''.join('+' if i < half else '-' for i in range(n))

    # str2: 前 1/3 是 '+', 中间 1/3 是 '-', 剩下是 '?'
    third = n // 3
    str2 = []
    for i in range(n):
        if i < third:
            str2.append('+')
        elif i < 2 * third:
            str2.append('-')
        else:
            str2.append('?')
    str2 = ''.join(str2)

    value = 0
    value_2 = 0
    unknown = 0
    for x in str1:
        if x == '+':
            value += 1
        else:
            value -= 1
    for x in str2:
        if x == '+':
            value_2 += 1
        elif x == '-':
            value_2 -= 1
        else:
            unknown += 1
    plus_count = 0
    minus_count = 0
    rav = 0
    x = value - value_2
    if abs(x) <= unknown:
        if x >= 0:
            plus_count += x
            rav = unknown - plus_count
        else:
            minus_count += x
            rav = unknown - minus_count
        if plus_count == 0 and minus_count == 0 and rav == 0:
            print('1.000000000000')
        else:
            if rav % 2 == 0:
                rav = int(rav / 2)
                plus_count += rav
                minus_count += rav
                k = max(plus_count, minus_count)
                C = math.factorial(unknown) / (math.factorial(unknown - k) * math.factorial(k))
                O = math.pow(2, unknown)
                res = C / O
                print(f'{res:.12f}')
            else:
                print('0.000000000000')
    else:
        print('0.000000000000')


if __name__ == "__main__":
    main(10)