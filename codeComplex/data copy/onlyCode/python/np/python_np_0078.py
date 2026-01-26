from math import factorial, pow


def wifi(s1, s2):
    count1, count2, count3 = 0, 0, 0
    for i in range(len(s1)):
        if s1[i] == '+':
            count1 += 1
        elif s1[i] == '-':
            count2 += 1
        if s2[i] == "+":
            count1 -= 1
        elif s2[i] == '-':
            count2 -= 1
        else:
            count3 += 1
    if count1 < 0 or count2 < 0:
        return '{:.9f}'.format(0)
    q = factorial(count1 + count2) / (factorial(count1) * factorial(count2))
    r = q / pow(2, count3)
    return r


t1 = input()
t2 = input()
print(wifi(t1, t2))
