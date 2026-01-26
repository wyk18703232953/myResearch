import math

def main(n):
    # Deterministic generation of s and t based on n
    # s: first half '+' (ceil), second half '-' (floor)
    s = ''.join('+' if i < (n + 1) // 2 else '-' for i in range(n))
    # t: first n//3 positions '+', next n//3 positions '-', rest '?'
    third = n // 3
    t = ''.join(
        '+' if i < third else
        '-' if i < 2 * third else
        '?' for i in range(n)
    )

    p = 0
    for c in s:
        if c == '+':
            p += 1

    pt, qt = 0, 0
    for c in t:
        if c == '+':
            pt += 1
        elif c == '?':
            qt += 1

    req = p - pt
    if req > qt or req < 0:
        ans = 0
    else:
        ans = math.factorial(qt) / math.factorial(req)
        ans /= math.factorial(qt - req)
        ans /= pow(2, qt)

    print(ans)


if __name__ == "__main__":
    main(10)