def comp(a, b):
    x = len(a)
    s1 = ''
    s2 = ''
    for i in range(x):
        s1 += str(a[i])
        s2 += str(b[i])
    if s1 > s2:
        return 1

    else:
        return 0


def main(n):
    # Deterministically generate two digit strings a_str and b_str
    # Let lengths depend on n
    len_a = n
    len_b = n  # keep equal length to exercise the more complex branch

    # Generate digits in a simple periodic pattern
    a_str = ''.join(str((i * 3 + 1) % 10) for i in range(len_a))
    b_str = ''.join(str((i * 7 + 2) % 10) for i in range(len_b))

    a = list(a_str)
    b = list(b_str)
    cnt = [0] * 10
    n_len = len(a)
    m_len = len(b)
    sol = ''
    for i in range(n_len):
        a[i] = int(a[i])
        cnt[a[i]] += 1

    if n_len != m_len:
        a.sort(reverse=True)
        for i in a:
            sol += str(i)
        # print(sol)
        pass

    else:
        a.sort()
        for i in range(n_len):
            b[i] = int(b[i])
        for i in range(n_len - 1):
            for j in range(i, n_len):
                if a[i] < a[j]:
                    temp = a[i]
                    a[i] = a[j]
                    a[j] = temp
                    if comp(a, b):
                        temp = a[i]
                        a[i] = a[j]
                        a[j] = temp
        for i in a:
            sol += str(i)
        # print(sol)
        pass
if __name__ == "__main__":
    main(10)