from math import factorial


def C(k, n):
    return factorial(n) // factorial(k) // factorial(n - k)


def generate_inputs(n):
    # n controls the length of the strings
    length = max(1, n)

    # s1: first half '+', second half '-'
    half = length // 2
    s1 = '+' * half + '-' * (length - half)

    # s2: alternate '+', '?', '-', cycling
    pattern = ['+', '?', '-']
    s2 = ''.join(pattern[i % 3] for i in range(length))

    return s1, s2


def main(n):
    s1, s2 = generate_inputs(n)
    n1 = s1.count('+')
    n2 = s2.count('+')
    n3 = s2.count('?')
    if n2 > n1:
        print(0)
    else:
        try:
            print(C(n1 - n2, n3) / (2 ** n3))
        except Exception:
            print(0)


if __name__ == "__main__":
    main(10)