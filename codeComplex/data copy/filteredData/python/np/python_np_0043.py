from math import factorial

def main(n):
    # Generate deterministic strings s and s1 based on n
    # s: string with '+' and '-' of length n
    # s1: string with '+', '-', and '?' of length n
    s = ''.join('+' if i % 2 == 0 else '-' for i in range(n))
    s1 = ''.join(
        '+' if i % 3 == 0 else '-' if i % 3 == 1 else '?'
        for i in range(n)
    )

    plus = s.count('+') - s1.count('+')
    minus = s.count('-') - s1.count('-')
    q = s1.count('?')

    if plus < 0 or minus < 0:
        result = 0.0
    else:
        result = (factorial(q) / factorial(q - plus) / factorial(plus)) * (0.5 ** q)
    print(result)
    return result

if __name__ == "__main__":
    main(10)