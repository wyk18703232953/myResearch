from math import factorial
import random

def main(n):
    s1 = ''.join(random.choice(['+', '-']) for _ in range(n))
    s2 = ''.join(random.choice(['+', '-', '?']) for _ in range(n))
    unknown = 0
    x1 = 0
    for c in s1:
        if c == '+':
            x1 += 1
        else:
            x1 -= 1
    x2 = 0
    for c in s2:
        if c == '+':
            x2 += 1
        elif c == '?':
            unknown += 1
        else:
            x2 -= 1
    x = abs(x1 - x2)
    if x > unknown:
        return 0
    elif x == unknown:
        return 1 / 2 ** unknown
    else:
        if (unknown - x) % 2 == 1:
            return 0
        else:
            return (factorial(unknown) // (factorial((unknown - x) // 2) * factorial(unknown - (unknown - x) // 2))) / 2 ** unknown

if __name__ == "__main__":
    print(main(10))