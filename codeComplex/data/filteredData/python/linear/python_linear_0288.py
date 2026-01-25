from collections import defaultdict

def main(n):
    # n: number of strings; each string length is n
    # deterministic generation of parentheses strings
    s = []
    for i in range(n):
        # pattern: first half '(', second half ')', with slight variation by i
        chars = []
        for j in range(n):
            if j % 2 == 0:
                # even positions depend on i and j
                if (i + j) % 3 == 0:
                    chars.append('(')
                else:
                    chars.append(')')
            else:
                # odd positions depend on i and j in another way
                if (i * 2 + j) % 4 < 2:
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

    print(ans)


if __name__ == "__main__":
    # example call; adjust n as needed for experiments
    main(10)