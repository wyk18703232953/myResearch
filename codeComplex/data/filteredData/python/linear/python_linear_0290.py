def main(n):
    from collections import defaultdict

    # deterministic generation of n strings of parentheses
    # pattern: mix of balanced, left-heavy, right-heavy, and random-like but deterministic
    strs = []
    for i in range(n):
        # choose a simple deterministic pattern based on i
        t = i % 4
        length = (i % 10) + 1  # length between 1 and 10
        if t == 0:
            # mostly '(' then ')'
            s = "(" * length + ")" * (length // 2)
        elif t == 1:
            # mostly ')' then '('
            s = ")" * (length // 2) + "(" * length
        elif t == 2:
            # alternating starting with '('
            s = "".join("(" if j % 2 == 0 else ")" for j in range(length))
        else:
            # alternating starting with ')'
            s = "".join(")" if j % 2 == 0 else "(" for j in range(length))
        strs.append(s)

    first = defaultdict(int)
    second = defaultdict(int)
    for s in strs:
        count = 0
        min_count = 0
        for c in s:
            if c == '(':
                count += 1
            else:
                count -= 1
            if count < min_count:
                min_count = count
        if min_count >= 0:
            first[count] += 1
        if count == min_count:
            second[count] += 1

    res = 0
    for k, v in first.items():
        res += v * second[-k]

    return res


if __name__ == "__main__":
    # example deterministic run
    print(main(10))