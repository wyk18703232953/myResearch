from collections import defaultdict

def generate_parentheses_strings(n):
    # Deterministically generate n parentheses strings
    # Pattern: cycle through some base patterns and expand with index
    base_patterns = ["()", ")(", "(())", "(()", "())", "(((", ")))", "()(())", "())(()", "()()"]
    res = []
    for i in range(n):
        base = base_patterns[i % len(base_patterns)]
        # Expand deterministically based on i to vary lengths
        extra_open = i % 3
        extra_close = (i // 3) % 3
        s = "(" * extra_open + base + ")" * extra_close
        res.append(s)
    return res

def core_logic(strings):
    one = defaultdict(lambda: 0)
    two = defaultdict(lambda: 0)

    for el in strings:
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

    return ans

def main(n):
    # n controls the number of input strings
    strings = generate_parentheses_strings(n)
    result = core_logic(strings)
    # print(result)
    pass
if __name__ == "__main__":
    # Example call; you can change the value of n for different scales
    main(10)