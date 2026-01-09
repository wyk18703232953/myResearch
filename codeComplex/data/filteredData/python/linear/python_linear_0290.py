def main(n):
    from collections import defaultdict

    # Deterministically generate n strings of parentheses
    # Example pattern: for i in range(n), build a string of length (i % (n+1)) + 1
    # characters chosen by a simple rule based on i and j
    strings = []
    for i in range(n):
        length = (i % (n + 1)) + 1
        s_chars = []
        for j in range(length):
            if (i + j) % 2 == 0:
                s_chars.append('(')

            else:
                s_chars.append(')')
        strings.append(''.join(s_chars))

    first = defaultdict(int)
    second = defaultdict(int)
    for s in strings:
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

    # print(res)
    pass
if __name__ == "__main__":
    main(1000)