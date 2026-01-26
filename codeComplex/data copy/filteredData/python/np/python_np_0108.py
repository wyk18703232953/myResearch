from math import factorial as fact

def main(n):
    # Interpret n as the length of the strings s and t
    if n < 1:
        n = 1

    # Deterministically construct s and t of length n
    # Pattern for s: cycle '+', '-', '+', '-', ...
    s = ''.join('+' if i % 2 == 0 else '-' for i in range(n))

    # Pattern for t: for first n//3 positions use '?', then mimic s
    split = n // 3
    t = ''.join('?' if i < split else s[i] for i in range(n))

    pos = s.count('+') - t.count('+')
    neg = s.count('-') - t.count('-')
    que = t.count('?')

    if pos < 0 or neg < 0 or pos + neg != que:
        print(0)
    else:
        result = (fact(que) / (fact(pos) * fact(neg))) / (2 ** que)
        print(result)

if __name__ == "__main__":
    main(10)