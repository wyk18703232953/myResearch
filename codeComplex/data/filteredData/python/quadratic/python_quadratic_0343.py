def main(n):
    # Generate deterministic test data based on n
    # s and t will both be strings of length n, composed from 'a'..'z'
    # and guaranteed to be anagrams so the core logic runs.
    if n <= 0:
        print(-1)
        return

    # Deterministically construct s and t
    chars = [chr(ord('a') + (i % 26)) for i in range(n)]
    s = ''.join(chars)
    # Create t by a deterministic permutation of s:
    # for example, rotate by (n // 2)
    shift = n // 2
    t_chars = [chars[(i + shift) % n] for i in range(n)]
    t = ''.join(t_chars)

    sl = [i for i in s]
    tl = [i for i in t]
    ans = []
    if ''.join(sorted(s)) != ''.join(sorted(t)):
        print(-1)
    else:
        for i in range(n):
            if sl[i] != tl[i]:
                for j in range(i + 1, n):
                    if sl[j] == tl[i]:
                        break
                for k in range(j - 1, i - 1, -1):
                    sl[k], sl[k + 1] = sl[k + 1], sl[k]
                    ans.append(k + 1)
        print(len(ans))
        for i in ans:
            print(i, end=' ')


if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(10)