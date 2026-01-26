import itertools

def compute_probability(s1, s2):
    kol1 = {'+': 0, '-': 0, '?': 0}
    kol2 = {'+': 0, '-': 0, '?': 0}

    for s in s1:
        kol1[s] += 1

    for s in s2:
        kol2[s] += 1

    if kol1['+'] == kol2['+'] and kol1['-'] == kol2['-']:
        return 1.0

    mod1 = kol1['+'] - kol1['-']
    mod2 = kol2['+'] - kol2['-']
    mod3 = abs(mod2 - mod1)
    if mod3 > kol2['?']:
        return 0.0

    list_comb = [1, -1]
    sum_pos = 0
    col = 0
    for comb in itertools.product(list_comb, repeat=kol2['?']):
        if sum(comb) == mod3:
            sum_pos += 1
        col += 1

    return sum_pos / col


def generate_inputs(n):
    if n <= 0:
        return "+", "+"

    base = n
    plus_count_s1 = base // 2
    minus_count_s1 = base - plus_count_s1

    plus_count_s2 = base // 3
    minus_count_s2 = base // 3
    q_count_s2 = base - plus_count_s2 - minus_count_s2

    s1 = "+" * plus_count_s1 + "-" * minus_count_s1
    s2 = "+" * plus_count_s2 + "-" * minus_count_s2 + "?" * q_count_s2
    return s1, s2


def main(n):
    s1, s2 = generate_inputs(n)
    ans = compute_probability(s1, s2)
    print(ans)


if __name__ == "__main__":
    main(10)