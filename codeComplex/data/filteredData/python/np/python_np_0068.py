from math import factorial

def main(n):
    # 构造确定性的输入 s 和 s1，长度与 n 相关
    # s: 前 n//2 个为 '+', 后面为 '-'
    # s1: 前 n//3 个为 '+', 中间 n//3 个为 '-', 剩余为 '?'
    if n < 1:
        n = 1
    s = ''.join('+' if i < n // 2 else '-' for i in range(n))
    s1 = ''.join(
        '+' if i < n // 3 else
        '-' if i < 2 * n // 3 else
        '?'
        for i in range(n)
    )

    pos1 = 0
    pos = 0
    posi = 0
    negi = 0
    posi1 = 0
    negi1 = 0
    ques1 = 0

    for i in s:
        if i == '+':
            pos += 1
            posi += 1
        else:
            pos -= 1
            negi += 1

    for i in s1:
        if i == '+':
            posi1 += 1
        elif i == '-':
            negi1 += 1
        else:
            ques1 += 1

    if posi == posi1 and negi == negi1:
        print(1)
        return

    diff1 = posi - posi1
    diff = negi - negi1
    if diff < 0 or diff1 < 0:
        print(0)
    else:
        outcomes = 2 ** ques1
        nume = factorial(ques1)
        deno = factorial(ques1 - diff1) * factorial(diff1)
        fav1 = nume / deno
        ques1 = ques1 - diff1
        num1 = factorial(ques1)
        deno1 = factorial(ques1 - diff) * factorial(diff)
        fav2 = num1 / deno1
        ans = fav1 * fav2
        print(ans / outcomes)


if __name__ == "__main__":
    main(10)