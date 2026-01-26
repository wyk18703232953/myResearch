from math import factorial as fact

def main(n):
    # Deterministically generate s and t based on n
    # s: first n positions are '+', next n positions are '-'
    # t: pattern of '+', '-', '?' with period 3 over length 2n
    s = '+' * n + '-' * n
    chars = ['+', '-', '?']
    t = ''.join(chars[i % 3] for i in range(2 * n))

    pos = s.count('+') - t.count('+')
    neg = s.count('-') - t.count('-')
    que = t.count('?')
    if pos < 0 or neg < 0:
        print(0)
    else:
        print((fact(que) / (fact(pos) * fact(neg))) / (2 ** que))

if __name__ == "__main__":
    main(5)