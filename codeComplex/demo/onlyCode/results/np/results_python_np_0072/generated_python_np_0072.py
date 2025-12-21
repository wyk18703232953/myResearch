from math import factorial
import random

def main(n):
    s1 = ''.join(random.choice(['+','-']) for _ in range(n))
    s2 = []
    for _ in range(n):
        r = random.random()
        if r < 1/3:
            s2.append('+')
        elif r < 2/3:
            s2.append('-')
        else:
            s2.append('?')
    s2 = ''.join(s2)

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

    n = s2.count('?')
    diff = abs(finPos - stPos)
    if diff > n:
        return 0
    elif (n & 1) != (diff & 1):
        return 0
    else:
        i = 0
        for i in range(n // 2, n):
            if i * 2 - n == diff:
                break
        if i * 2 - n != diff:
            i += 1
        return (factorial(n) / (factorial(n - i) * factorial(i))) / (1 << n)

if __name__ == "__main__":
    print(main(10))