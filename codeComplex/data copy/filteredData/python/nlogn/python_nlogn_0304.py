def main(n):
    # Deterministically generate lst of length n
    lst = [i % (n + 3) + 1 for i in range(n)]
    # Deterministically generate s of length 2*n with exactly n '0' and n '1'
    # Pattern: first '0' at even positions until we reach n zeros, rest are '1'
    s_list = []
    zeros = 0
    ones = 0
    for i in range(2 * n):
        if zeros < n and (i % 2 == 0 or ones >= n):
            s_list.append('0')
            zeros += 1

        else:
            s_list.append('1')
            ones += 1
    s = ''.join(s_list)

    for j in range(n):
        lst[j] = [lst[j], j + 1]
    lst.sort()
    stk = []
    i = 0
    out = []
    for j in range(2 * n):
        if s[j] == '0':
            stk.append(lst[i][1])
            out.append(str(lst[i][1]))
            i += 1

        else:
            out.append(str(stk[-1]))
            stk.pop()
    # print(" ".join(out))
    pass
if __name__ == "__main__":
    main(5)