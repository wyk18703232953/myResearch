def main(n):
    # Deterministically generate s and t of length n over small alphabet
    # Alphabet: 'a', 'b', 'c', 'd'
    alphabet = ['a', 'b', 'c', 'd']
    s = [alphabet[i % 4] for i in range(n)]
    # Generate t as a deterministic permutation of s using a simple pattern
    # Here we rotate indices by (n // 3 + 1) to get a permutation
    shift = n // 3 + 1
    t = [''] * n
    for i in range(n):
        t[(i + shift) % n] = s[i]

    # Core algorithm logic from original code
    s_list = s[:]  # work on a copy
    t_str = ''.join(t)

    if sorted(s_list) != sorted(t_str):
        # print(-1)
        pass
        return

    lst = [0] * n
    s_work = s_list[:]
    for i in range(n):
        for j in range(n):
            if s_work[j] == t_str[i]:
                lst[j] = i + 1
                s_work[j] = "."
                break

    ans = 0
    a = []
    for i in range(n):
        for j in range(n - 1):
            if i != j:
                if lst[j] > lst[j + 1]:
                    ans += 1
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]
                    a.append(j + 1)

    # print(ans)
    pass

    if a:
        # print(*a)
        pass

    else:
        # print()
        pass
if __name__ == "__main__":
    main(10)