import math

def main(n):
    # n 表示字符串长度
    if n <= 0:
        return

    # 构造 sone：前半部分是 '+', 后半部分是 '-'
    half = n // 2
    sone = ['+' if i < half else '-' for i in range(n)]

    # 构造 stwo：
    # 按周期 3 生成 '+', '-', '?'
    pattern = ['+', '-', '?']
    stwo = [pattern[i % 3] for i in range(n)]

    sum1 = 0
    sum2 = 0
    m = 0
    for i in range(len(sone)):
        if sone[i] == '+':
            sum1 = sum1 + 1
            m = m + 1
        else:
            sum1 = sum1 - 1

    k = 0
    for i in range(len(stwo)):
        if stwo[i] == '+':
            sum2 = sum2 + 1
            k = k
        elif stwo[i] == '-':
            sum2 = sum2 - 1
            k = k
        elif stwo[i] == '?':
            k = k + 1

    n_local = 0
    if (k - (abs(sum1 - sum2))) < 0:
        print(float(0))
    elif (k - (abs(sum1 - sum2))) == 0:
        if k == 0:
            print(float(1))
        else:
            print(float(pow(0.5, k)))
    else:
        n_local = k - (abs(sum1 - sum2))
        n_local = abs(sum1 - sum2) + n_local / 2
        if abs(sum1 - sum2) == 0:
            print(float((math.factorial(k) / (math.factorial(k / 2) * math.factorial(k / 2))) * pow(0.5, k)))
        else:
            print(float((math.factorial(k) / (math.factorial(k - n_local) * math.factorial(n_local))) * pow(0.5, k)))


if __name__ == "__main__":
    main(10)