def main(n):
    # Deterministically generate s and t of length n
    # Example pattern: s is repeating 'abc', t is s shifted by 1 with wrap
    base_chars = ['a', 'b', 'c']
    s_list = [base_chars[i % 3] for i in range(n)]
    t_list = [base_chars[(i + 1) % 3] for i in range(n)]
    s = ''.join(s_list)
    t = ''.join(t_list)

    dic, diff = {}, []
    res, res1, res2 = 0, -1, -1
    for i in range(n):
        if s[i] != t[i]:
            res += 1
            diff.append(i)
            dic[t[i]] = i
    swap1, swap2 = False, False
    for i in diff:
        if s[i] in dic:
            swap1 = True
            res1 = i + 1
            j = dic[s[i]]
            res2 = j + 1
            if s[j] == t[i]:
                swap2 = True
                break
    # print(res - (2 if swap2 else 1 if swap1 else 0))
    pass
    # print(res1, res2)
    pass
if __name__ == "__main__":
    main(10)