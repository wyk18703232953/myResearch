def main(n):
    # Deterministically generate a binary string s of length n using pattern over '0','1','2'
    chars = ['0', '1', '2']
    s = ''.join(chars[i % 3] for i in range(n))

    c = s.count('1')
    c1, i = 0, 0
    while i < len(s) and s[i] != '2':
        if s[i] == '0':
            c1 += 1
        i += 1

    # Collect output in a list for determinism and to avoid interleaved prints
    out = []
    out.append('0' * c1)
    out.append('1' * c)
    while i < len(s):
        if s[i] != '1':
            out.append(s[i])
        i += 1

    result = ''.join(out)
    # print(result)
    pass
if __name__ == "__main__":
    # Example deterministic call; adjust n for different input scales
    main(20)