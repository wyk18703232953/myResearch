def main(n):
    # ensure n is at least 1
    if n <= 0:
        return
    # deterministically generate s and t as permutations over first n lowercase letters
    # s: 'abc...'(first n letters)
    # t: reverse of s
    from string import ascii_lowercase
    # repeat alphabet if n > 26
    base = ascii_lowercase
    # construct s_chars deterministically
    s_chars = [base[i % 26] for i in range(n)]
    t_chars = list(reversed(s_chars))
    s = "".join(s_chars)
    t = "".join(t_chars)

    if sorted(s) != sorted(t):
        print(-1)
        return
    s = list(s)
    t = list(t)
    ans = []
    for i in range(n):
        for j in range(i, n - 1):
            if s[j + 1] == t[i]:
                for k in range(j, i - 1, -1):
                    ans.append(k + 1)
                    s[k + 1], s[k] = s[k], s[k + 1]
                break
    print(len(ans))
    if ans:
        print(*ans)


if __name__ == "__main__":
    # example deterministic call; adjust n as needed for experiments
    main(10)