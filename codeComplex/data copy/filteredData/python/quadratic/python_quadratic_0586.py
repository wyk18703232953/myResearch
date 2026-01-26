def mismatch(s1, s2):
    cnt = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            cnt += 1
    return cnt

def solve_single_case(n, k, s):
    from math import ceil
    check = ''
    for _ in range(ceil((k + 2) / 3)):
        check += 'RGB'
    ls = []
    for i in range(3):
        ls.append(check[i:i + k])
    m = n
    for i in range(n - k + 1):
        for j in ls:
            m = min(m, mismatch(s[i:i + k], j))
    return m

def generate_input_structure(n):
    if n < 3:
        n = 3
    T = n
    cases = []
    for t in range(T):
        length = 3 + (t % 5)
        k = 1 + (t % length)
        s_chars = []
        for i in range(length):
            # deterministic pattern over 'R', 'G', 'B'
            v = (t + i) % 3
            if v == 0:
                s_chars.append('R')
            elif v == 1:
                s_chars.append('G')

            else:
                s_chars.append('B')
        s = ''.join(s_chars)
        cases.append((length, k, s))
    return T, cases

def main(n):
    T, cases = generate_input_structure(n)
    results = []
    for (length, k, s) in cases:
        res = solve_single_case(length, k, s)
        results.append(str(res))
    # print("\n".join(results))
    pass
if __name__ == "__main__":
    main(10)