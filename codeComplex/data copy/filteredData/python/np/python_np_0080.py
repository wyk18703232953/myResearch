from math import factorial

def calc_arrangement(n, m):
    return factorial(n) / factorial(n - m)

def calc_combination(n, m):
    return calc_arrangement(n, m) / factorial(m)

def generate_strings(n):
    # We choose total length L = n + 1 (so that n = number of '?' in str2)
    L = n + 1
    str1 = []
    str2 = []
    for i in range(L):
        # str1: alternate '+' and '-'
        if i % 2 == 0:
            str1.append('+')
        else:
            str1.append('-')
        # str2: first n positions are '?', last one determined to control diff
        if i < n:
            str2.append('?')
        else:
            # Last position of str2 chooses from '+', '-', '?'
            # in a deterministic pattern based on n
            if n % 3 == 0:
                str2.append('+')
            elif n % 3 == 1:
                str2.append('-')
            else:
                str2.append('?')
    return str1, str2

def main(n):
    str1, str2 = generate_strings(n)

    count_unknown = 0
    diff = 0

    for i in range(len(str1)):
        if str1[i] == '+':
            diff += 1
        else:
            diff -= 1
        if str2[i] == '+':
            diff -= 1
        elif str2[i] == '-':
            diff += 1
        else:
            count_unknown += 1

    if count_unknown == 0:
        if diff == 0:
            print(1.0)
        else:
            print(0.0)
    elif count_unknown < abs(diff):
        print(0.0)
    else:
        m = (count_unknown - diff) / 2
        if m < 0 or m != int(m):
            print(0.0)
        else:
            m = int(m)
            res = calc_combination(count_unknown, m) * (0.5 ** count_unknown)
            print(res)

if __name__ == "__main__":
    main(5)