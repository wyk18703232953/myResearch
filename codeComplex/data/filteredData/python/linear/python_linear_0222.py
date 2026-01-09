def main(n):
    # Generate deterministic binary string s of length n
    # Pattern: first char '1', others alternate '0' and '1'
    if n <= 0:
        return
    s_chars = ['1'] + [('0' if i % 2 == 0 else '1') for i in range(1, n)]
    s = ''.join(s_chars)

    if n == 1:
        # print(s)
        pass

    else:
        zeros = s.count('0')
        # print('1' + zeros * '0')
        pass
if __name__ == "__main__":
    main(10)