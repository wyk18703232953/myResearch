def main(n):
    # Input structure:
    # original: n, s (len n), t (len n, anagram of s)
    # We deterministically generate s and t based on n.

    # Generate s as a repeating pattern of lowercase letters, length n
    base = [chr(ord('a') + (i % 26)) for i in range(n)]
    s = base[:]  # list of chars

    # Generate t as a deterministic permutation of s that preserves multiset:
    # simple rule: reverse blocks of size k where k = max(1, n // 3)
    k = max(1, n // 3) if n > 0 else 1
    t_list = []
    for i in range(0, n, k):
        block = s[i:i + k]
        t_list.extend(block[::-1])
    t = ''.join(t_list)

    # Core algorithm from original program
    s_work = s[:]            # work on a copy
    t_work = t               # string
    i, r = 0, []

    if sorted(s_work) != sorted(t_work):
        print(-1)
    else:
        while i < n:
            j = i
            while j < n and s_work[j] != t_work[i]:
                j += 1
            s_work[i:j + 1] = s_work[j:j + 1] + s_work[i:j]
            r.extend(range(j, i, -1))
            i += 1
        print(len(r))
        if r:
            print(*r)


if __name__ == "__main__":
    # example deterministic call; adjust n as needed for experiments
    main(10)