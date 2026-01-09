from collections import defaultdict

def main(n):
    s = []
    for i in range(n):
        # Deterministic generation of parentheses strings
        # Mix of '()' and ')(' patterns with varying lengths
        length = (i % 10) + 1
        if i % 3 == 0:
            el = ''.join('()'[(j + i) % 2] for j in range(length))
        elif i % 3 == 1:
            el = ''.join('()'[j % 2] for j in range(length))

        else:
            el = ''.join('()'[(j // 2) % 2] for j in range(length))
        s.append(el)

    one = defaultdict(lambda: 0)
    two = defaultdict(lambda: 0)

    for el in s:
        I = 0
        min_ = 0

        for char in el:
            I += {'(': 1, ')': -1}[char]
            min_ = min(min_, I)

        if I >= 0 and min_ == 0:
            one[I] += 1

        if I <= 0 and min_ == I:
            two[I] += 1

    ans = 0
    for el in one.keys():
        ans += one[el] * two[-el]

    # print(ans)
    pass
if __name__ == "__main__":
    main(1000)