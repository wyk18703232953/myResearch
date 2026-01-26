import math

def factorial(num):
    if num == 1:
        return num
    else:
        return num * factorial(num - 1)

def generate_inputs(n):
    # n controls the length of s1 and s2
    length = max(1, n)

    # Generate s1 deterministically using '+', '-' pattern
    # Example pattern: "+-++-+..." depending on i
    s1_chars = []
    for i in range(length):
        if (i // 2) % 2 == 0:
            s1_chars.append('+')
        else:
            s1_chars.append('-')
    s1 = ''.join(s1_chars)

    # Generate s2 deterministically using '+', '-', '?' pattern
    # Use i % 3 to cycle through characters
    s2_chars = []
    for i in range(length):
        r = i % 3
        if r == 0:
            s2_chars.append('+')
        elif r == 1:
            s2_chars.append('-')
        else:
            s2_chars.append('?')
    s2 = ''.join(s2_chars)

    return s1, s2

def experiment(s1, s2):
    ans = 0
    for i in range(0, len(s1)):
        if s1[i] == '+':
            ans += 1
        else:
            ans -= 1
    t = 0
    qm = 0
    for i in range(0, len(s2)):
        if s2[i] == '+':
            t += 1
        elif s2[i] == '-':
            t -= 1
        else:
            qm += 1
    if qm == 0:
        if ans == t:
            print(1.000000000000)
        else:
            print(0.000000000000)
    else:
        k = ans - t
        if abs(k) == qm:
            na = 1 / pow(2, qm)
            print(na)
        elif abs(k) > qm:
            print(0.000000000000)
        else:
            if (k % 2 == 0 and qm % 2 == 1):
                print(0.000000000000)
            elif (k % 2 == 1 and qm % 2 == 0):
                print(0.000000000000)
            else:
                a = abs((qm + k) / 2)
                b = abs((qm - k) / 2)
                nu = factorial(qm) / (factorial(a) * factorial(b))
                ans_val = nu / (pow(2, qm))
                print(ans_val)

def main(n):
    s1, s2 = generate_inputs(n)
    experiment(s1, s2)

if __name__ == "__main__":
    main(10)