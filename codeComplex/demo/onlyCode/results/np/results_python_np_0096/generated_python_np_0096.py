import math
def main(n):
    s1 = ('+' * (n // 2)) + ('-' * (n - n // 2))
    if n % 3 == 0:
        s2 = '+' * (n // 3) + '-' * (n // 3) + '?' * (n - 2 * (n // 3))
    else:
        s2 = '+' * (n // 3) + '-' * (n // 3) + '?' * (n - 2 * (n // 3))
    if s2.count('?') == 0:
        if s1.count('+') == s2.count('+') and s1.count('-') == s2.count('-'):
            p = 1
        else:
            p = 0
    else:
        if (s1.count('+') < s2.count('+') != 0) or (s1.count('-') == 0 < s2.count('-') != 0):
            p = 0
        else:
            pl = s1.count('+') - s2.count('+')
            mi = s1.count('-') - s2.count('-')
            p = (math.factorial((pl + mi)) / math.factorial(pl) / math.factorial(mi)) / 2 ** (pl + mi)
    print('%1.9f' % p)
    return p

if __name__ == "__main__":
    main(10)