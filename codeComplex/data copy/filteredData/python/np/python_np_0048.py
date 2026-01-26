from math import factorial

def main(n):
    # 生成确定性的 s1 和 s2，长度与 n 线性相关
    # s1: 前半部分为 '+', 后半部分为 '-'
    len_s = max(1, n)
    s1 = ''.join('+' if i < len_s // 2 else '-' for i in range(len_s))

    # s2: 循环使用 '+', '-', '?'
    pattern = ['+', '-', '?']
    s2 = ''.join(pattern[i % 3] for i in range(len_s))

    missing = 0
    x1 = 0
    for ch in s1:
        if ch == '+':
            x1 += 1
        else:
            x1 -= 1

    x2 = 0
    for ch in s2:
        if ch == '+':
            x2 += 1
        elif ch == '?':
            missing += 1
        else:
            x2 -= 1

    x = abs(x1 - x2)
    if x > missing:
        result = 0.0
    elif x == missing:
        result = 1 / (2 ** missing)
    else:
        if (missing - x) % 2 == 1:
            result = 0.0
        else:
            k = (missing - x) // 2
            comb = factorial(missing) // (factorial(k) * factorial(missing - k))
            result = comb / (2 ** missing)
    print(result)


if __name__ == "__main__":
    main(10)