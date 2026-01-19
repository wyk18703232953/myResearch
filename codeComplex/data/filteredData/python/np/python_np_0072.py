from math import factorial

def main(n):
    # n controls the length of the two strings
    # s1: first n//2 characters are '+', rest are '-'
    # s2: first n//3 '+', next n//3 '-', rest '?'
    if n <= 0:
        return
    half = n // 2
    third = n // 3

    s1 = ''.join('+' if i < half else '-' for i in range(n))
    s2 = ''.join(
        '+' if i < third else
        '-' if i < 2 * third else
        '?'
        for i in range(n)
    )

    finPos = 0
    for c in s1:
        if c == '+':
            finPos += 1
        else:
            finPos -= 1

    stPos = 0
    for c in s2:
        if c == '+':
            stPos += 1
        elif c == '-':
            stPos -= 1

    cnt_q = s2.count('?')
    diff = abs(finPos - stPos)

    if diff > cnt_q:
        print(0)
    elif (cnt_q & 1) != (diff & 1):
        print(0)
    else:
        i = 0
        for i in range(cnt_q // 2, cnt_q):
            if i * 2 - cnt_q == diff:
                break
        if i * 2 - cnt_q != diff:
            i += 1
        ans = (factorial(cnt_q) / (factorial(cnt_q - i) * factorial(i))) / (1 << cnt_q)
        print(ans)


if __name__ == "__main__":
    main(10)