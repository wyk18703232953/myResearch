from math import inf

def main(n):
    # Generate two deterministic binary strings of length n
    a = [0, 0]
    s0 = ''.join('0' if i % 2 == 0 else '1' for i in range(n))
    s1 = ''.join('1' if (i * 3) % 5 < 2 else '0' for i in range(n))
    a[0] = [c for c in s0]
    a[1] = [c for c in s1]

    an = [-inf, -inf, -inf]
    if a[0][0] == a[1][0] == '0':
        an[0] = 0
    elif a[0][0] != a[1][0]:
        an[1] = 0
    x = 0
    for i in range(1, len(a[0])):
        if an[0] == 0:
            if a[0][i] == a[1][i] == '0':
                x += 1
                an = [-inf, 0, -inf]
            elif a[0][i] != a[1][i]:
                x += 1
                an = [-inf] * 3

            else:
                an = [-inf, -inf, -inf]
        elif an[1] == 0:
            if a[0][i] == a[1][i] == '0':
                x += 1
                an = [-inf, -inf, -inf]
            elif a[0][i] != a[1][i]:
                pass

            else:
                an = [-inf, -inf, -inf]

        else:
            if a[0][i] == a[1][i] == '0':
                an = [0, -inf, -inf]
            elif a[0][i] != a[1][i]:
                an = [-inf, 0, -inf]

            else:
                an = [-inf, -inf, -inf]
    # print(x)
    pass
if __name__ == "__main__":
    main(10)