from math import factorial
import random

def calc_arrangement(n, m):
    return factorial(n) / factorial(n - m)

def calc_combination(n, m):
    return calc_arrangement(n, m) / factorial(m)

def main(n):
    # 通过规模 n 生成测试数据：
    # 生成长度为 n 的目标串 str1，只含 '+' 或 '-'
    # 生成长度为 n 的观测串 str2，含 '+', '-', '?' 三种
    choices_str1 = ['+', '-']
    choices_str2 = ['+', '-', '?']

    str1 = [random.choice(choices_str1) for _ in range(n)]
    str2 = [random.choice(choices_str2) for _ in range(n)]

    diff = 0
    unknown = 0

    for i in range(n):
        if str1[i] == '+':
            diff += 1
        else:
            diff -= 1

        if str2[i] == '+':
            diff -= 1
        elif str2[i] == '-':
            diff += 1
        else:  # '?'
            unknown += 1

    if unknown == 0:
        if diff == 0:
            res = 1.0
        else:
            res = 0.0
    elif unknown < abs(diff):
        res = 0.0
    else:
        # (n - diff) 必须为偶数，否则组合数无意义，在原逻辑中仍会给出 0 结果
        if (unknown - diff) % 2 != 0:
            res = 0.0
        else:
            k = (unknown - diff) // 2
            res = calc_combination(unknown, k) * (0.5 ** unknown)

    print(res)
    return res

if __name__ == "__main__":
    # 示例：使用规模 n=10 运行一次
    main(10)