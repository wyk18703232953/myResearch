def substring(x, s):
    count = 0
    ans = 0

    for i in range(x):
        if s[i] == "x":
            count += 1

        else:
            if count >= 3:
                ans += count - 2
            count = 0
    if count >= 3:
        ans += count - 2

    return ans


def main(n):
    x = n
    # Deterministically generate a string of length n
    # Pattern: blocks of 'x' of increasing length separated by 'a'
    chars = []
    current = 1
    while len(chars) < x:
        block_len = min(current, x - len(chars))
        chars.extend('x' for _ in range(block_len))
        if len(chars) < x:
            chars.append('a')
        current += 1
    s = ''.join(chars[:x])
    result = substring(x, s)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)