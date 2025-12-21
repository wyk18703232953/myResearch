from math import factorial as fact
import random

def main(n):
    signs = ['+', '-']
    s = ''.join(random.choice(signs) for _ in range(n))
    t_list = []
    for ch in s:
        r = random.random()
        if r < 0.7:
            t_list.append(ch)
        else:
            t_list.append('?')
    t = ''.join(t_list)
    pos = s.count('+') - t.count('+')
    neg = s.count('-') - t.count('-')
    que = t.count('?')
    if pos < 0 or neg < 0:
        return 0
    return (fact(que) / (fact(pos) * fact(neg))) / (2 ** que)

if __name__ == "__main__":
    print(main(10))