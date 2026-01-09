def main(n):
    # n controls the length of the target string t
    # pattern s will contain at most one '*'
    # make sure n >= 1
    if n < 1:
        n = 1

    # Construct n, m (lengths) deterministically
    # Let m be length of pattern s, choose m between 1 and n+1
    m = (n % 5) + 1  # m in [1,5]
    # Constrain t length so that algorithm has meaningful cases
    # Make t length between 1 and max(n, m+1)
    t_len = max(1, n)

    # Build pattern s deterministically with at most one '*'
    # Cases: no '*', '*' at start, '*' at end, '*' in middle
    mode = n % 4
    base_chars = ['a', 'b', 'c', 'd', 'e', 'f']

    if mode == 0:
        # no '*', length = m
        s_list = [base_chars[i % len(base_chars)] for i in range(m)]
    elif mode == 1:
        # '*' at start
        if m == 1:
            s_list = ['*']

        else:
            s_list = ['*'] + [base_chars[i % len(base_chars)] for i in range(m - 1)]
    elif mode == 2:
        # '*' at end
        if m == 1:
            s_list = ['*']

        else:
            s_list = [base_chars[i % len(base_chars)] for i in range(m - 1)] + ['*']

    else:
        # '*' in middle, if possible
        if m == 1:
            s_list = ['*']
        elif m == 2:
            s_list = ['*', base_chars[0]]

        else:
            ind = m // 2
            left = [base_chars[i % len(base_chars)] for i in range(ind)]
            right = [base_chars[(i + 1) % len(base_chars)] for i in range(m - ind - 1)]
            s_list = left + ['*'] + right

    s = ''.join(s_list)

    # Build target string t of length t_len deterministically
    t_list = [base_chars[(i + 2) % len(base_chars)] for i in range(t_len)]
    t = ''.join(t_list)

    # Now run original logic, with n,m as lengths of s,t
    n_len = len(s)
    m_len = len(t)

    if '*' not in s:
        if s == t:
            # print('YES')
            pass

        else:
            # print('NO')
            pass
    elif n_len > m_len + 1:
        # print('NO')
        pass
    elif n_len == 1 and s == '*':
        # print('YES')
        pass

    else:
        s_chars = list(s)
        t_chars = list(t)
        if s_chars[0] == '*':
            if s_chars[1:] == t_chars[-(len(s_chars[1:])):]:
                # print('YES')
                pass

            else:
                # print('NO')
                pass
        elif s_chars[-1] == '*':
            if s_chars[:n_len - 1] == t_chars[:n_len - 1]:
                # print('YES')
                pass

            else:
                # print('NO')
                pass

        else:
            ind = s_chars.index('*')
            if s_chars[:ind] == t_chars[:ind] and s_chars[ind + 1:] == t_chars[-len(s_chars[ind + 1:]):]:
                # print('YES')
                pass

            else:
                # print('NO')
                pass
if __name__ == "__main__":
    # Example deterministic calls for scaling
    for size in [1, 2, 5, 10, 50, 100]:
        main(size)