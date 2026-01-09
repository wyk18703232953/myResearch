from collections import defaultdict

def main(n):
    # Generate n deterministic parentheses strings
    # Pattern: for i in range(1, n+1), create a sequence of length i
    # using '(' if (j // 2) % 2 == 0 else ')', which is deterministic.
    s = []
    for i in range(1, n + 1):
        chars = []
        for j in range(i):
            if (j // 2) % 2 == 0:
                chars.append('(')

            else:
                chars.append(')')
        s.append(''.join(chars))

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
    main(10)