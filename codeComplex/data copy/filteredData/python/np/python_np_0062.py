import math

def solve(s, s1):
    plus = s.count('+') - s1.count('+')
    minus = s.count('-') - s1.count('-')
    v = s1.count('?')
    if plus < 0 or minus < 0:
        return 0.0
    return (math.factorial(v) / math.factorial(v - plus) / math.factorial(plus)) * (0.5 ** v)

def main(n):
    if n <= 0:
        n = 1
    half = n // 2
    s = ''.join('+' if i % 2 == 0 else '-' for i in range(n))
    s1 = ''.join('?' if i < half else ('+' if i % 2 == 0 else '-') for i in range(n))
    result = solve(s, s1)
    print(result)

if __name__ == "__main__":
    main(10)