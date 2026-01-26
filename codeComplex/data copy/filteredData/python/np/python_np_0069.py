from math import factorial

def main(n):
    # Deterministically generate s and new based on n
    # s: first n positions, pattern '+', '-', '+', '-', ...
    # new: next n positions, pattern '+', '-', '?', repeated
    pattern_s = ['+', '-']
    pattern_new = ['+', '-', '?']
    s = ''.join(pattern_s[i % 2] for i in range(n))
    new = ''.join(pattern_new[i % 3] for i in range(n))

    questions = 0
    plus = s.count('+')
    minus = s.count('-')
    for ch in new:
        if ch == '+':
            plus -= 1
        elif ch == '-':
            minus -= 1
        else:
            questions += 1
    if plus < 0 or minus < 0:
        print(0)
    else:
        num = factorial(questions) / (factorial(plus) * factorial(minus))
        den = 2 ** questions
        print("{0:.10f}".format(num / den))

if __name__ == "__main__":
    main(10)