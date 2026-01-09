def main(n):
    # Generate a deterministic string s of length n
    # Pattern: '+' if i % 3 != 0 else '-'
    s = ''.join('+' if i % 3 != 0 else '-' for i in range(n))

    maxn = 0
    now = 0
    for i in s:
        if i == '+':
            now += 1

        else:
            now -= 1
        if -now > maxn:
            maxn = -now
    result = now + maxn
    # print(result)
    pass
if __name__ == "__main__":
    main(10)